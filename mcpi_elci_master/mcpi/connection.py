import socket
import select
import sys
from mcpi.util import flatten_parameters_to_bytestring
import rsa # import RSA module
from rsa.key import PublicKey
import base64

""" @author: Aron Nieminen, Mojang AB"""
class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.lastSent = ""
        self.publicKey = None  # Add publicKey attribute

    def mEncrypted (self, f, msg):
        self.send(f, msg)

    def encryption(self, message, publicKey):
        # Encrypt the message with the PublicKey object
        ciphertext = rsa.encrypt(message, publicKey)

        # Return the base64-encoded ciphertext
        return base64.b64encode(ciphertext).decode('ascii')
    
    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  "Drained Data: <%s>\n"%data.strip()
            e += "Last Message: <%s>\n"%self.lastSent.strip()
            sys.stderr.write(e)

    def send(self, f, *data):
        print("SEND FUNCTION WORK")
        """
        Sends data. Note that a trailing newline '\n' is added here

        The protocol uses CP437 encoding - https://en.wikipedia.org/wiki/Code_page_437
        which is mildly distressing as it can't encode all of Unicode.
        """
        print("Public Key: ", self.publicKey)

        # Encrypt s with public key
        encrypted_data = self.encryption(flatten_parameters_to_bytestring(data),self.publicKey)
        print("Encrypted Data: ", encrypted_data)

        s = b"".join([f, b"(", encrypted_data.encode('ascii'), b")", b"\n"])

        # call _send function
        self._send(s)

    def _send(self, s):
        """
        The actual socket interaction from self.send, extracted for easier mocking
        and testing
        """
        self.drain()
        self.lastSent = s
        self.socket.sendall(s)

    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError("%s failed"%self.lastSent.strip())
        
        # Convert the received public key string to bytes
        public_key_bytes = base64.b64decode(s.encode('ascii'))

        # Convert the public key bytes to PEM format
        pem_data = rsa.pem.save_pem(public_key_bytes, 'PUBLIC KEY')

        # Load the public key from the PEM data
        self.publicKey = rsa.key.PublicKey.load_pkcs1_openssl_pem(pem_data)
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()

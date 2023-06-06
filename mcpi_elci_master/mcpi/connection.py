import socket
import select
import sys
from .util import flatten_parameters_to_bytestring
import rsa # import RSA module
import base64

""" @author: Aron Nieminen, Mojang AB"""

global global_private_key
class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.lastSent = ""

    def mEncrypted (self, f, msg):
        self.send(f, msg)

    def keyGenerate(self):
    # To generate public key and private key
        (publicKey, privateKey) = rsa.newkeys(2048) #rsa.newskeys(number_of_bits)

        # save publicKey in file
        with open('public_key.pem', mode='wb') as public_file:
            # Saves the key in PKCS#1 PEM format.
            public_file.write(publicKey.save_pkcs1('PEM'))

        # save privateKey in file
        with open('private_key.pem', mode='wb') as private_file:
            # Saves the key in PKCS#1 PEM format.
            private_file.write(privateKey.save_pkcs1('PEM'))

    def keyLoad(self):
        # load publicKey from file
        with open('public_key.pem', mode='rb') as public_file:
            # Loads a key in PKCS#1 PEM format.
            publicKey = rsa.PublicKey.load_pkcs1(public_file.read())

        # load privateKey from file
        with open('private_key.pem', mode='rb') as private_file:
            # Loads a key in PKCS#1 PEM format.
            privateKey = rsa.PrivateKey.load_pkcs1(private_file.read())

        return publicKey, privateKey

    def encryption(self, message, publicKey):
        # # Print message
        # print("Message: ", message)
        
        # message_encode = bytes(message, 'utf-8')

        # Encryption only happen if len(message_encode) <= rsa.common.byte_size(publicKey.n):
        # Encrypt the encoded message with publicKey into ciphertext
        ciphertext = rsa.encrypt(message, publicKey)

        print("Ciphertext: ", base64.b64encode(ciphertext))

        return base64.b64encode(ciphertext)

    def decryption(self, ciphertext, privateKey):

        try:
            # Decrypt the ciphertext with private key to get the encoded message
            message_encode = rsa.decrypt(ciphertext, privateKey)

            # return decoded message
            return message_encode.decode('ascii')
        except:
            return 'Error'
    
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
        # Generate public and private key
        self.keyGenerate()

        # Get public and private key
        publicKey, global_private_key = self.keyLoad()

        # Encrypt s with public key
        encrypted_data = self.encryption(flatten_parameters_to_bytestring(data),publicKey)

        s = b"".join([f, b"(", encrypted_data, b")", b"\n"])

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
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()

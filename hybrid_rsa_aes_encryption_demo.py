from Crypto.Cipher import AES
import rsa, secrets, base64

def encryptAES(cipherAES, plaintext):
    return cipherAES.encrypt(plaintext.encode('ascii'))

def decryptAES(cipherAES, ciphertext):
    return cipherAES.decrypt(ciphertext).decode('ascii')

def keyGenerate():
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

def keyLoad():
    # load publicKey from file
    with open('public_key.pem', mode='rb') as public_file:
        # Loads a key in PKCS#1 PEM format.
        publicKey = rsa.PublicKey.load_pkcs1(public_file.read())

    # load privateKey from file
    with open('private_key.pem', mode='rb') as private_file:
        # Loads a key in PKCS#1 PEM format.
        privateKey = rsa.PrivateKey.load_pkcs1(private_file.read())

    return publicKey, privateKey

def encryption(message, publicKey):
    # Encode message into ASCII format (bytes)
    message_encode = message.encode('ascii')

    # Encryption only happen if len(message_encode) == rsa.common.byte_size(publicKey.n):
    # Encrypt the encoded message with publicKey into ciphertext
    ciphertext = rsa.encrypt(message_encode, publicKey)

    return ciphertext

def decryption(ciphertext, privateKey):
    try:
        # Decrypt the ciphertext with private key to get the encoded message
        message_encode = rsa.decrypt(ciphertext, privateKey)

        # Return decoded message
        return message_encode.decode('ascii')
    except:
        return 'Error'

if __name__ == "__main__":
    # Generate public and private keys with RSA.
    keyGenerate()
    # Get public and private key with RSA.
    publicKey, privateKey = keyLoad()

    # Generate a 32-byte (256-bit) random key for AES encryption and encoded as base64 to represented it as an ASCII string
    key = secrets.token_bytes(32)
    print('AES Symmetric key: ', key)
    AESkey = base64.b64encode(key).decode('ascii')

    plaintext = input("Type message here:")
    cipherAES = AES.new(key, AES.MODE_EAX)
    # Retrieves the value of the nonce (number used once) from the AES cipher object cipherAES
    nonce = cipherAES.nonce 
    # Encrypt the plaintext using the AES cipher in EAX mode.
    ciphertext = encryptAES(cipherAES, plaintext)
    print(f'Ciphertext: {ciphertext}')

    # Encrypt the AES key with RSA public key
    cipherKey = encryption(AESkey, publicKey)
    print('==========================ENCRYPTION COMPLETE==========================')

    # Decrypt the AES key with RSA private key
    decryptkey = decryption(cipherKey, privateKey)
    # Decode the decrypted AES key from base64 to bytes
    decryptedK = base64.b64decode(decryptkey)
    # The decrypted AES key is used to create an AES cipher object
    cipherAESd = AES.new(decryptedK, AES.MODE_EAX, nonce=nonce)
    # Decrypt the ciphertext with the AES cipher object 'cipherAESd'
    plaintext = decryptAES(cipherAESd, ciphertext)
    print(f'Plaintext: {plaintext}')
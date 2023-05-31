import rsa # import RSA module

# FIX THIS: Overflow error happen when message size not equal to public key size

def keyGenerate():
    # To generate public key and private key
    (pubicKey, privateKey) = rsa.newkeys(2048) #rsa.newskeys(number_of_bits)

    # save publicKey in file
    with open('public_key.pem', mode='wb') as public_file:
        # Saves the key in PKCS#1 PEM format.
        public_file.write(pubicKey.save_pkcs1('PEM'))

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

        # return decoded message
        return message_encode.decode('ascii')
    except:
        return 'Error'
    
if __name__ == "__main__":

    message = input("Type here:")

    # Generate public and private keys
    keyGenerate()
    # Get public and private key
    publicKey, privateKey = keyLoad()

    # Encrypt message
    c = encryption(message, publicKey)

    print(f'ciphertext: {c}\n')

    # Decrypt message
    m = decryption(c, privateKey)

    print(f'message: {m}\n')

import hmac
import hashlib
import time
from mcpi.minecraft import Minecraft

# Assignment 3 main file
# Feel free to modify, and/or to add other modules/classes in this or other files


#HMAC EXAMPLE
def create_hmac_for_file(file_path, secret_key):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    hmac_obj = hmac.new(secret_key.encode(), file_data, hashlib.sha256)
    return hmac_obj.hexdigest()

# You can use the function like this:
secret_key = 'mysecretkey'
file_path = "C:/Users/Edward/Downloads/testing.txt" # replace with your file path
hmac_result = create_hmac_for_file(file_path, secret_key)

print(f'HMAC for the file from the sender: {hmac_result}')
def verify_hmac_for_file(file_path, received_hmac, secret_key):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    hmac_obj = hmac.new(secret_key.encode(), file_data, hashlib.sha256)
    calculated_hmac = hmac_obj.hexdigest()

    return hmac.compare_digest(calculated_hmac, received_hmac)

# Use the function:
secret_key = 'mysecretkey'
file_path = "C:/Users/Edward/Downloads/testing.txt" # replace with your file path
received_hmac = hmac_result  # replace with the received HMAC
verification_result = verify_hmac_for_file(file_path, received_hmac, secret_key)
print(f'HMAC for the file from the receiver: {received_hmac}')
if verification_result:
    print('The message is authentic and unaltered.')
else:
    print('The message is not authentic or has been tampered with.')
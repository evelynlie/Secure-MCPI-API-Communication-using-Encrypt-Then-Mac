import hmac
import hashlib
import time
from mcpi.minecraft import Minecraft

# Assignment 3 main file
# Feel free to modify, and/or to add other modules/classes in this or other files


#HMAC EXAMPLE
#The timestamp is combined with the file's data. The timestamp is unique for each second, thus giving a different HMAC every second. 
#Please be aware that by doing this, you are no longer verifying the integrity of just the file, but rather the file combined with the timestamp.
def create_hmac_for_file(file_path, secret_key):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    timestamp = str(time.time()).encode()
    data = file_data + timestamp

    hmac_obj = hmac.new(secret_key.encode(), data, hashlib.sha256)
    return hmac_obj.hexdigest()

# Use the function:
secret_key = 'mysecretkey'
file_path = "C:/Users/Edward/Downloads/testing.txt" # replace with your file path
hmac_result = create_hmac_for_file(file_path, secret_key)
print(f'HMAC for the file: {hmac_result}')
import os
import random
import base64

from cryptokrm import *

append_data = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
key = os.urandom(16)

def test_func(message):
    data = ''.join((message,append_data))

    cipher = AES.new(key,AES.MODE_ECB)
    data = pkcs7padding(data,16)
    return cipher.encrypt(data)

# Step 1: Determine block size

# Step 2: Detect ECB mode

# Step 3: Craft input block 1 byte short

# Step 4: Dictionary of possible last bytes

# Step 5: 

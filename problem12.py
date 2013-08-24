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
append_len=len(test_func(''))
test_str = ''
for i in xrange(64):
    test_output = test_func(test_str)
    if len(test_output) > append_len:
        blocksize = len(test_output) - append_len
        print "Block size is", blocksize
        break
    test_str += 'A'

# Step 2: Detect ECB mode

# Step 3: Craft input block 1 byte short

# Step 4: Dictionary of possible last bytes

# Step 5: Match output of step 3 to entry in step 5

# Step 6: Loop to step 3 for next byte

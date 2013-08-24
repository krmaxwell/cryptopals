import os
import random
import base64

from cryptokrm import *

secret_data = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

key = os.urandom(16)

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def test_func(message):
    data = ''.join((message,secret_data))

    cipher = AES.new(key,AES.MODE_ECB)
    data = pkcs7padding(data,16)
    return cipher.encrypt(data)

def detect_ecb():
    plaintext = ' ' * 1024
    tempdict = dict()
    flag = False

    ciphertext = test_func(plaintext)
    data = list(chunks(ciphertext,16))

    for block in data:
        if block in tempdict:
            flag = True
            break
        else:
            tempdict[block] = True

    return flag
    
# Step 1: Determine block size
secret_len=len(test_func(''))
test_str = ''
for i in xrange(64):
    test_output = test_func(test_str)
    if len(test_output) > secret_len:
        blocksize = len(test_output) - secret_len
        print "Block size is", blocksize
        break
    test_str += 'A'

# Step 2: Detect ECB mode
print "Function uses ECB?", detect_ecb()

# Step 3: Craft input block 1 byte short
test_block = 'A' * (blocksize-1)
test_out = test_func(test_block)[:blocksize]

# Step 4: Dictionary of possible last bytes
test_dict = dict()
for c in xrange(256):
    input_block = test_block + chr(c)
    test_dict[input_block] = test_func(input_block)[:blocksize]

# Step 5: Match output of step 3 to entry in step 5
for block in test_dict:
    if test_out == test_dict[block]:
        print "Candidate character is %c - %03d" % (block[-1],ord(block[-1]))

# Step 6: Loop to step 3 for next byte

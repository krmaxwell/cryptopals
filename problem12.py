import os
import sys
import random
import base64

from cryptokrm import *


secret_data = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
key = os.urandom(16)
cipher = AES.new(key, AES.MODE_ECB)


def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def oracle(message):
    data = ''.join((message, secret_data))
    data = pkcs7padding(data, 16)
    return cipher.encrypt(data)


def detect_ecb():
    plaintext = ' ' * 1024
    tempdict = dict()
    flag = False

    ciphertext = oracle(plaintext)
    data = list(chunks(ciphertext, 16))

    for block in data:
        if block in tempdict:
            flag = True
            break
        else:
            tempdict[block] = True

    return flag


def main():
    decrypt = ''
    # Step 1: Determine block size
    secret_len = len(oracle(''))
    test_str = ''
    for i in xrange(64):
        test_output = oracle(test_str)
        if len(test_output) > secret_len:
            blocksize = len(test_output) - secret_len
            print "Block size is", blocksize
            break
        test_str += 'A'

    # Step 2: Detect ECB mode
    print "Function uses ECB?", detect_ecb()

    # Step 3: Craft input block 1 byte short
    guess_block = 'A' * (blocksize-(index+1)) + decrypt + chr(c)
    guess_result = oracle(guess_block)[:blocksize]
    test_block = 'A' * (blocksize-(index+1))
    test_result = oracle(test_block)[(i / blocksize)*blocksize:((i/blocksize)+1)*blocksize]
    print guess_block.encode('hex'),len(guess_block),test_block.encode('hex'),len(test_block)
    if guess_result == test_result:
        sys.stdout.write(chr(c))
        decrypt = decrypt + chr(c)
        break

    # Step 4: Match result from test input to all possible vals for that byte
    print

if __name__ == "__main__":
    main()

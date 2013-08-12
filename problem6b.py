#!/usr/bin/python

import base64
import sys

from cryptokrm import *

with open('data/data6.txt','rb') as f:
    message = f.read()

ctext = base64.b64decode(message)

# user-defined keysize
k = int(sys.argv[1])

# now split cipher
btext = [0]*k

fullkey = ''

for i in xrange(0,k):
    btext[i] = ctext[i::k]
    for key in xrange(0,256):
        cleardata = ''
        for j in xrange(0,len(btext[i])):
            data = ord(btext[i][j]) ^ key
            if data in xrange(32,127) or data == 10 or data == 13:
                cleardata += chr(data)
            else:
                break
        if len(cleardata) == len(btext[0]):
            fullkey += chr(key)

print fullkey

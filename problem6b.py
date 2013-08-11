#!/usr/bin/python

import base64
import sys

from cryptokrm import *

with open('data/data6.txt','rb') as f:
    message = f.read()

# user-defined keysize
k = sys.argv[1]

# now split cipher
btext = [0]*k

for i in xrange(0,k):
    btext[i] = ctext[i::k]

#print [b.encode('hex') for b in btext]
#print btext[0].encode('hex')
#print "----------"

# just for testing: first k worth of bytes
for key in xrange(0,256):
    cleardata = ''
    for i in xrange(0,len(btext[0])):
        data = ord(btext[0][i]) ^ key
        if data in xrange(32,128) or data == 10 or data == 13:
            cleardata += chr(data)
        else:
            break
    if len(cleardata) == len(btext[0]):
        print key, cleardata

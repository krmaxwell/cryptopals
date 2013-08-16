#!/usr/bin/python

import base64
import sys
import operator

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
    similarity=dict()
    for key in xrange(0,256):
        cleardata = ''
        for j in xrange(0,len(btext[i])):
            cleardata += chr(ord(btext[i][j]) ^ key)
        similarity[key] = cos_sim(asciifreq.values(),frequency(cleardata).values())
    best = max(similarity.iteritems(), key=operator.itemgetter(1))[0]
    fullkey += chr(best)
    
print fullkey
print fullkey.encode('hex')

print xorstr(ctext,fullkey)

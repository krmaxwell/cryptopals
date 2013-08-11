#!/usr/bin/python

import base64

from cryptokrm import *

with open('data6.txt','rb') as f:
    message = f.read()

# decode into ciphertext
ctext = base64.b64decode(message)
print "Ciphertext:\n",ctext.encode('hex')
print "----------"

min_k,min_d = 0,1000

for k in xrange(4,65): 
    # Hamming dist between block 1 and block 2
    d1 = float(hamming_dist(ctext[0:k],ctext[k:k*2])) / k
    # Hamming dist between block 2 and block 3
    d2 = float(hamming_dist(ctext[k:k*2],ctext[k*2:k*3])) / k
    # Hamming dist between block 3 and block 4
    d3 = float(hamming_dist(ctext[k*2:k*3],ctext[k*3:k*4])) / k
    d = (d1+d2+d3)/3
    if d < min_d:
        min_k, min_d = k,d

print "Probable keysize is %d with dist %f" % (min_k, min_d)
k = min_k

# now split cipher
btext = [0]*k

for i in xrange(0,k):
    btext[i] = ctext[i::k]

print [b.encode('hex') for b in btext]

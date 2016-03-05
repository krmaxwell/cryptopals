#!/usr/bin/python

import base64

from cryptokrm import *

with open('data/data6.txt','rb') as f:
    message = f.read()

# decode into ciphertext
ctext = base64.b64decode(message)

min_k,min_d = 0,1000

for k in xrange(2,40): 
    dists = []
    for n in xrange(len(ctext)/k-1):
        dists.append(float(hamming_dist(ctext[k*n:k*(n+1)],ctext[k*(n+1):k*(n*2)]))/k)
    d = sum(dists)
    print k,d
    if d < min_d:
        min_k, min_d = k,d

print "----------"
print "Probable keysize is %d with dist %.4f" % (min_k, min_d)

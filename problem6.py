#!/usr/bin/python

import base64

from cryptokrm import *

with open('data6.txt','rb') as f:
    message = f.read()

ctext = base64.b64decode(message)

min_k,min_d = 0,1000

for k in xrange(3,65): 
    d1 = float(hamming_dist(ctext[0:k-1],ctext[k:k*2-1])) / k
    d2 = float(hamming_dist(ctext[k:k*2-1],ctext[k*2:k*3-1])) / k
    d3 = float(hamming_dist(ctext[k*2:k*3-1],ctext[k*3:k*4-1])) / k
    d = (d1+d3+d2)/3
    if d < min_d:
        min_k, min_d = k,d

print "Probable keysize is %d with Hdist %f" % (min_k, min_d)

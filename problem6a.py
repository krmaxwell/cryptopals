#!/usr/bin/python

import base64

from cryptokrm import *

with open('data6.txt','rb') as f:
    message = f.read()

# decode into ciphertext
ctext = base64.b64decode(message)
#print "Ciphertext:\n",ctext.encode('hex')
#print "----------"

min_k,min_d = 0,1000

for k in xrange(2,40): 
    # Hamming dist between block 1 and block 2
    d1 = float(hamming_dist(ctext[k*0:k*1],ctext[k*1:k*2])) / k
    # Hamming dist between block 2 and block 3
    d2 = float(hamming_dist(ctext[k*2:k*3],ctext[k*3:k*4])) / k
    # Hamming dist between block 3 and block 4
    d3 = float(hamming_dist(ctext[k*4:k*5],ctext[k*5:k*6])) / k
    d = (d1+d2+d3)/3
    print k,d
    if d < min_d:
        min_k, min_d = k,d

print "----------"
print "Probable keysize is %d with dist %f" % (min_k, min_d)

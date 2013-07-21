#!/usr/bin/python

import sys
import binascii

ciphertext = long(sys.argv[1],base=16)
cipherdata = bytearray(binascii.unhexlify('%x' % ciphertext))

for key in xrange(0,256):
	cleardata=bytearray()
	for i in xrange(0,len(cipherdata)):
		data = cipherdata[i] ^ key
		if data in range(32,128):
			cleardata.append(cipherdata[i] ^ key)
		else:
			break
	if len(cleardata) == len(cipherdata):
		print cleardata

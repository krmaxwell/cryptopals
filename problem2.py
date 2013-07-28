#!/usr/bin/python

import sys
import base64

def strxor(s1, s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

dat1 = sys.argv[1].decode('hex')
dat2 = sys.argv[2].decode('hex')
print strxor(dat1,dat2).encode('hex')

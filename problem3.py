#!/usr/bin/python

import sys
import binascii
import re
from cryptokrm import *

message = sys.argv[1].decode('hex')
similarity = dict()

for key in xrange(0,256):
    candidate = xorstr(message,chr(key))
    similarity[key] = cos_sim(english.values(),frequency(candidate).values())
    if similarity[key] > 0.3:
        print "%3d %.4f" % (key, similarity[key])

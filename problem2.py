#!/usr/bin/python

import sys
import string
import base64

dat1 = long(sys.argv[1],base=16)
dat2 = long(sys.argv[2],base=16)
print hex(dat1^dat2)[2:-1]

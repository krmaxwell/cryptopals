#!/usr/bin/python

import sys
import string
import base64

data = long(sys.argv[1],base=16)
hexdat = base64.b16decode(hex(data)[2:-1],casefold=True)
output = base64.b64encode(hexdat)
print output


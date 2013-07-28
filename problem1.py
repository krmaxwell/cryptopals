#!/usr/bin/python

import sys
import base64

# first convert the string to actual binary data
data = long(sys.argv[1],base=16)

# hex() with a long type arg returns something of the form "0xc0ffee"
# so we slice out the part of hex() output we want
# this is effectively base16 per RFC 3548
hexdat = base64.b16decode(hex(data)[2:-1],casefold=True)

# hexdat is now a string containing the same bytes as data
# we did this becase b64encode() is annoying about input types
output = base64.b64encode(hexdat)
print output

# go back the other way: turn base64 into hex
print base64.b16encode(base64.b64decode(output))

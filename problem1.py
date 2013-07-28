#!/usr/bin/python

import sys
import base64

# first convert the string to actual binary data
data = sys.argv[1].decode('hex')

# hexdat is now a string containing the same bytes as data
# we did this becase b64encode() is annoying about input types
output = base64.b64encode(data)
print output

# go back the other way: turn base64 into hex
print base64.b16encode(base64.b64decode(output))

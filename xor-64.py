import sys
import base64

from cryptokrm import *

with open(sys.argv[1],'rb') as f:
    s = f.read()

print xorstr(base64.b64decode(s),sys.argv[2])

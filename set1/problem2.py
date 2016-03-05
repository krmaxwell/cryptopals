import sys
import base64

from cryptokrm import *

dat1 = sys.argv[1].decode('hex')
dat2 = sys.argv[2].decode('hex')
print xor(dat1,dat2).encode('hex')

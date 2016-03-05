import sys
from cryptokrm import *

message = sys.argv[1]
blocklen = int(sys.argv[2])
print message.encode('hex')
print pkcs7padding(message, blocklen).encode('hex')

import sys
from cryptokrm import *

message = sys.argv[1]
blocklen = sys.argv[2]
print message.encode('hex')
print pkcs7padding(message,key).encode('hex')

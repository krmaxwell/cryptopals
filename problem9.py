from cryptokrm import *

message = "YELLOW SUBMARINE"
print message.encode('hex')
print pkcs7padding(message,20).encode('hex')

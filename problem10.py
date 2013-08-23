import base64
from Crypto.Cipher import AES

with open('gettysburg.txt','rb') as f:
  s = f.read()

data = base64.b64decode(s)

key = "YELLOW SUBMARINE"
cipher = AES.new(key,AES.MODE_ECB)
iv = binascii.unhexlify('%02d' % chr(0)) * len(key)

for i in xrange(len(s) / len(key)):

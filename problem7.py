import base64
from Crypto.Cipher import AES

with open('data/data7.txt','rb') as f:
  s = f.read()

cipher = AES.new('YELLOW SUBMARINE',AES.MODE_ECB)
print cipher.decrypt(base64.b64decode(s))

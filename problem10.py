import base64

from cryptokrm import *

with open('data/data10.txt','rb') as f:
  s = f.read()

data = base64.b64decode(s)

print cbcdecrypt(data,"YELLOW SUBMARINE")

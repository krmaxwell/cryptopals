from cryptokrm import *

with open('gettysburg.txt','rb') as f:
    s = f.read()

for i in xrange(16):
    print encryption_oracle(s).encode('hex')

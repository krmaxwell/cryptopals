#!/usr/bin/python
def strxor(s1, s2):
    if len(s1)==len(s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    return False

def xorstr(message, key):
    if len(key) < len(message):
        ekey = (key * (len(message)/len(key)+1))[:len(message)]
    else:
        ekey = key

    return strxor(message,ekey)

s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

hexdat = xorstr(s,"ICE").encode('hex')
answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
print hexdat
print hexdat == answer

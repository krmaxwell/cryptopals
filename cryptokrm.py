# An assortment of functions useful in crypto

def xor(s1, s2):
    if len(s1)==len(s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    return False

def xorstr(message, key):
    if len(key) < len(message):
        ekey = (key * (len(message)/len(key)+1))[:len(message)]
    else:
        ekey = key

    return xor(message,ekey)

def hamming_dist(s1,s2):
    s = strxor(s1,s2)
    bits = 0

    if s: # they are in fact the same length
        for c in s:
            bits += sum(bit == '1' for bit in bin(ord(c))[2:]) 
        return bits
    else:
        return False

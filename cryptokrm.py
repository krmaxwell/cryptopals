import numpy as np
import re

english = {'a' : 8.127, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702, 'f' : 2.228, 'g' : 2.015, 'h' : 6.094, 'i' : 6.966, 'j' : 0.153, 'k' : 0.747, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 'p' : 1.929, 'q' : 0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 'u' : 2.758, 'v' : 1.037, 'w' : 2.365, 'x' : 0.150, 'y' : 1.974, 'z' : 0.074} 
nullfreq = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0} 

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
    s = xor(s1,s2)
    bits = 0

    if s: # they are in fact the same length
        for c in s:
            bits += sum(bit == '1' for bit in bin(ord(c))[2:]) 
        return bits
    else:
        return False

def cos_sim(v1, v2): 
    return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))

def frequency(message):
    freq = nullfreq # prepopulate

    data = re.sub('[^a-z]','',message.lower()) # all we care about are letters
    for char in data:
        freq[char] = data.count(char) 

    length = len(data) 
    total = 0

    for x in freq: # iterate over keys
        if length > 0:
            freq[x] = (float(freq[x]) / length) * 100.0
        else:
            freq[x] = float(0)

    return freq



#!/usr/bin/python

import base64
import operator

from cryptokrm import *

def tastes_like_english(str):
    english_freq = {'E': 0.104, 'T': 0.072, 'A': 0.065, 'O': 0.059, 'N': 0.056, 'I': 0.055, 'S': 0.051, 'R': 0.049, 'H': 0.049, 'D': 0.034}
    freq_tot = float(0)
    for c in str:
        if c in english_freq:
            freq_tot += english_freq[c]
    freq_tot /= len(str)
    return freq_tot


def vigenere(ctext, key):
    ptext = ''
    if len(key) < len(message):
        ekey = (key * (len(message)/len(key)+1))[:len(message)]
    else:
        ekey = key
    for c in ctext:
        c

with open('vig.txt') as f:
    message = f.read()


# decode into ciphertext
ctext = message.replace(' ', '').replace('\n', '')
print ctext

min_k,min_d = 0,1000

for k in xrange(2,40): 
    dists = []
    for n in xrange(len(ctext)/k-1):
        dists.append(float(hamming_dist(ctext[k*n:k*(n+1)],ctext[k*(n+1):k*(n*2)]))/k)
    d = sum(dists)
    if d < min_d:
        min_k, min_d = k,d

print "Probable keysize is %d with distance %.4f" % (min_k, min_d)

k = min_k

# now split cipher
btext = [0]*k

fullkey = ''

for i in xrange(k):
    btext[i] = ctext[i::k]
    similarity = {}
    for key in xrange(26):
        cleardata = ''
        for j in xrange(0,len(btext[i])):
            new_c = ord(btext[i][j]) + key + 1
            if new_c > 90:
                new_c -= 26
            cleardata += chr(new_c)
        similarity[key] = tastes_like_english(cleardata)
    best = max(similarity.iteritems(), key=operator.itemgetter(1))[0]
    print "Position %x best match is %x with cossim %.3f" % (i, best, similarity[best])
    fullkey += chr(best+65)

print fullkey

print vigenere(ctext, fullkey)

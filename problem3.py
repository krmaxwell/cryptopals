#!/usr/bin/python

import sys
import binascii

words = set()

with open('dictionary.txt','rb') as wordfile:
	for word in wordfile.read().split('\n'): 
		words.add(word.upper())

ciphertext = long(sys.argv[1],base=16)
cipherdata = bytearray(binascii.unhexlify('%x' % ciphertext))

def is_english(message):
	word_t = 0.5			# expected fraction of words in message
	wordcount = 0
	wordalikes = 0

	for word in message.split():
		wordalikes += 1
		if word.upper() in words:
			wordcount += 1

	return float(wordcount) / wordalikes >= word_t
	

for key in xrange(0,256):
	cleardata=bytearray()
	for i in xrange(0,len(cipherdata)):
		data = cipherdata[i] ^ key # ciphertext known to be XORed with single character
		if data in xrange(32,128): # filter unprintable characters
			cleardata.append(cipherdata[i] ^ key)
		else:
			break
	if (len(cleardata) == len(cipherdata)) and is_english(cleardata.decode()):
		print "%3d " % key, cleardata

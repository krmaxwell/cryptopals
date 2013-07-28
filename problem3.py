#!/usr/bin/python

import sys
import binascii

words = set()

with open('dictionary.txt','rb') as wordfile:
	for word in wordfile.read().split('\n'): 
		words.add(word.upper())

cipherdata = sys.argv[1].decode('hex')

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
	cleardata=''
	for i in xrange(0,len(cipherdata)):
		data = ord(cipherdata[i]) ^ key # ciphertext known to be XORed with single character
		if data in xrange(32,128): # filter unprintable characters
			cleardata += chr(data)
		else:
			break
	if (len(cleardata) == len(cipherdata)) and is_english(cleardata.decode()):
		print "%3d " % key, cleardata

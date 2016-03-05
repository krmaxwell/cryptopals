#!/usr/bin/python

import sys
import operator

from cryptokrm import *

message = sys.argv[1].decode('hex')
similarity = dict()

fullkey = ''

for key in xrange(0,256):
    candidate = xorstr(message,chr(key))
    similarity[key] = cos_sim(asciifreq.values(),frequency(candidate).values())

best = max(similarity.iteritems(), key=operator.itemgetter(1))[0]
print best

print xorstr(message,chr(best))

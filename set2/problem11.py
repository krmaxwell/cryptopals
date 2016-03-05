from cryptokrm import *
from collections import Counter


def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

data = []
cipher_texts = []
plain_text = ' ' * 1024

# Generate chosen plaintexts
for i in xrange(16):
    cipher_texts.append(encryption_oracle(plain_text, debug=True))
print '----------------'

# first break each ciphertext into blocks of 16 bytes (128 bits)
for t in cipher_texts:
    data.append(list(chunks(t, 16)))

# now look for repeated blocks within each ciphertext
for text in data:
    tempdict = dict()
    flag = False
    counts = Counter()
    for block in text:
        counts[block] += 1
    for block in counts:
        if counts[block] > 1:
            flag = True
    if flag:
        print "ECB"
    else:
        print "CBC"

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

with open('gettysburg-oracle.txt','rb') as f:
    cipher_texts = f.readlines()

data = []
# first break each ciphertext into blocks of 16 bytes (128 bits)
for t in cipher_texts:
    data.append(list(chunks(t,16)))

# now look for repeated blocks within each ciphertext
for text in data:
    tempdict = dict()
    flag = False
    for block in text:
        if block in tempdict:
            tempdict[block] += 1
        else:
            tempdict[block] = 1
    for block in tempdict:
        if tempdict[block] > 1:
            flag = True
    if flag:
        print "ECB"
    else:
        print "CBC"

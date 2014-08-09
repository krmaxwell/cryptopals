import numpy as np
import binascii
import os
import random

from Crypto.Cipher import AES

english = {'a': 8.127, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.747, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 1.037, 'w': 2.365, 'x': 0.150, 'y': 1.974, 'z': 0.074}

# initialize ascii frequency
asciifreq = dict()
for i in xrange(256):
    asciifreq[i] = 0

# next values are taken from http://reusablesec.blogspot.com/2009/05/character-frequency-analysis-info.html
asciifreq[ord('a')] = 7.52766
asciifreq[ord('e')] = 7.0925
asciifreq[ord('o')] = 5.17
asciifreq[ord('r')] = 4.96032
asciifreq[ord('i')] = 4.69732
asciifreq[ord('s')] = 4.61079
asciifreq[ord('n')] = 4.56899
asciifreq[ord('1')] = 4.35053
asciifreq[ord('t')] = 3.87388
asciifreq[ord('l')] = 3.77728
asciifreq[ord('2')] = 3.12312
asciifreq[ord('m')] = 2.99913
asciifreq[ord('d')] = 2.76401
asciifreq[ord('0')] = 2.74381
asciifreq[ord('c')] = 2.57276
asciifreq[ord('p')] = 2.45578
asciifreq[ord('3')] = 2.43339
asciifreq[ord('h')] = 2.41319
asciifreq[ord('b')] = 2.29145
asciifreq[ord('u')] = 2.10191
asciifreq[ord('k')] = 1.96828
asciifreq[ord('4')] = 1.94265
asciifreq[ord('5')] = 1.88577
asciifreq[ord('g')] = 1.85331
asciifreq[ord('9')] = 1.79558
asciifreq[ord('6')] = 1.75647
asciifreq[ord('8')] = 1.66225
asciifreq[ord('7')] = 1.621
asciifreq[ord('y')] = 1.52483
asciifreq[ord('f')] = 1.2476
asciifreq[ord('w')] = 1.24492
asciifreq[ord('j')] = 0.836677
asciifreq[ord('v')] = 0.833626
asciifreq[ord('z')] = 0.632558
asciifreq[ord('x')] = 0.573305
asciifreq[ord('q')] = 0.346119
asciifreq[ord('A')] = 0.130466
asciifreq[ord('S')] = 0.108132
asciifreq[ord('E')] = 0.0970865
asciifreq[ord('R')] = 0.08476
asciifreq[ord('B')] = 0.0806715
asciifreq[ord('T')] = 0.0801223
asciifreq[ord('M')] = 0.0782306
asciifreq[ord('L')] = 0.0775594
asciifreq[ord('N')] = 0.0748134
asciifreq[ord('P')] = 0.073715
asciifreq[ord('O')] = 0.0729217
asciifreq[ord('I')] = 0.070908
asciifreq[ord('D')] = 0.0698096
asciifreq[ord('C')] = 0.0660872
asciifreq[ord('H')] = 0.0544319
asciifreq[ord('G')] = 0.0497332
asciifreq[ord('K')] = 0.0460719
asciifreq[ord('F')] = 0.0417393
asciifreq[ord('J')] = 0.0363083
asciifreq[ord('U')] = 0.0350268
asciifreq[ord('W')] = 0.0320367
asciifreq[ord('.')] = 0.0316706
asciifreq[ord('!')] = 0.0306942
asciifreq[ord('Y')] = 0.0255073
asciifreq[ord('*')] = 0.0241648
asciifreq[ord('@')] = 0.0238597
asciifreq[ord('V')] = 0.0235546
asciifreq[ord('-')] = 0.0197712
asciifreq[ord('Z')] = 0.0170252
asciifreq[ord('Q')] = 0.0147064
asciifreq[ord('X')] = 0.0142182
asciifreq[ord('_')] = 0.0122655
asciifreq[ord('$')] = 0.00970255
asciifreq[ord('#')] = 0.00854313
asciifreq[ord(',')] = 0.00323418
asciifreq[ord('/')] = 0.00311214
asciifreq[ord('+')] = 0.00231885
asciifreq[ord('?')] = 0.00207476
asciifreq[ord(';')] = 0.00207476
asciifreq[ord('^')] = 0.00195272
asciifreq[ord(' ')] = 0.00189169
asciifreq[ord('%')] = 0.00170863
asciifreq[ord('~')] = 0.00152556
asciifreq[ord('=')] = 0.00140351
asciifreq[ord('&')] = 0.00134249
asciifreq[ord('`')] = 0.00115942
asciifreq[ord('\\')] = 0.00115942
asciifreq[ord(')')] = 0.00115942
asciifreq[ord(']')] = 0.0010984
asciifreq[ord('[')] = 0.0010984
asciifreq[ord(':')] = 0.000549201
asciifreq[ord('<')] = 0.000427156
asciifreq[ord('(')] = 0.000427156
asciifreq[ord('>')] = 0.000183067
asciifreq[ord('"')] = 0.000183067
asciifreq[ord('|')] = 0.000122045
asciifreq[ord('{')] = 0.000122045
asciifreq[ord('\'')] = 0.000122045


class KRM_Error(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def xor(s1, s2):
    if len(s1) == len(s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
    return False


def xorstr(message, key):
    if len(key) < len(message):
        ekey = (key * (len(message)/len(key)+1))[:len(message)]
    else:
        ekey = key

    return xor(message, ekey)


def hamming_dist(s1, s2):
    s = xor(s1, s2)
    bits = 0

    if s:  # they are in fact the same length
        for c in s:
            bits += sum(bit == '1' for bit in bin(ord(c))[2:])
        return bits
    else:
        return False


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.sqrt(np.dot(v1, v1)) * np.sqrt(np.dot(v2, v2)))


def frequency(message):
    # prepopulate to match asciifreq
    freq = dict()
    for i in xrange(256):
        freq[i] = 0

    # count actual frequency in message
    for char in message:
        freq[ord(char)] = message.count(char)

    length = len(message)
    total = 0

    # normalize to a ratio
    for x in freq:  # iterate over keys
        if length > 0:
            freq[x] = (float(freq[x]) / length) * 100.0
        else:
            freq[x] = float(0)

    return freq


def pkcs7padding(message, blocklength):
    padlength = blocklength - (len(message) % blocklength)
    if padlength == 0:
        return message
    pad = binascii.unhexlify('%02d' % padlength) * padlength
    return ''.join((message, pad))


def cbcencrypt(message, key, iv=0):
    if iv == 0:
        iv = binascii.unhexlify('%02d' % 0) * len(key)
    elif len(iv) != len(key):
        raise KRM_Exception('IV and key lengths do not match')

    cipher = AES.new(key, AES.MODE_ECB)
    data = ''
    m = pkcs7padding(message, len(key))

    if (len(m) % len(key)) == 0:
        cycles = len(m) / len(key)
    else:
        cycles = len(m) / len(key) + 1

    for i in xrange(cycles):
        block = m[i*len(key):(i+1)*len(key)]
        block = xor(block, iv)
        iv = cipher.encrypt(block)
        data = ''.join((data, iv))

    return data


def cbcdecrypt(message, key):
    iv = binascii.unhexlify('%02d' % 0) * len(key)
    cipher = AES.new(key, AES.MODE_ECB)
    data = ''

    # TODO: why doesn't it handle the first block correctly?
    for i in xrange(len(message) / len(key)):
        block = message[i*len(key):(i+1)*len(key)]
        new_iv = block
        block = xor(cipher.decrypt(block), iv)
        iv = new_iv
        data = ''.join((data, block))

    return data


def encryption_oracle(message, debug=False):
    key = os.urandom(16)
    modes = ['CBC', 'ECB']

    mode = random.choice(modes)
    if debug:
        print mode
    prepend_data = os.urandom(random.randrange(5, 10))
    append_data = os.urandom(random.randrange(5, 10))
    data = ''.join((prepend_data, message, append_data))

    if mode == 'CBC':
        iv = os.urandom(16)
        # cbcencrypt handles padding on its own
        return cbcencrypt(data, key, iv)
    else:
        cipher = AES.new(key, AES.MODE_ECB)
        # PyCrypto leaves that up to you
        data = pkcs7padding(data, 16)
        return cipher.encrypt(data)

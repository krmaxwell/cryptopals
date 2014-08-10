#!/usr/bin/env python
from collections import Counter
import numpy as np


english_freq = {'E': 0.104, 'T': 0.072, 'A': 0.065, 'O': 0.059, 'N': 0.056, 'I': 0.055, 'S': 0.051, 'R': 0.049, 'H': 0.049, 'D': 0.034}

cipher_text = "SZAPQFWWJESPCPLCPXZCPESLYAPZAWPHSZHTWWDZWPGESTD"


def tastes_like_english(str):
    freq_tot = float(0)
    for c in str:
        if c in english_freq:
            freq_tot += english_freq[c]
    freq_tot /= len(str)
    return freq_tot


def rot_n(n, text):
    new_str = ''
    for c in text:
        new_c = ord(c)+n
        if new_c > 90:
            new_c -= 26
        new_str = ''.join((new_str, chr(new_c)))
    return new_str


def main():
    max_freq = 0
    best_n = 0
    for n in xrange(26):
        candidate = rot_n(n+1, cipher_text)
        print candidate
        score = tastes_like_english(candidate)
        if score > max_freq:
            max_freq = score
            best_n = n+1
    print "Best is %d that yields %s" % (best_n, rot_n(best_n, cipher_text))


if __name__ == "__main__":
    main()

#! /usr/bin/python

from hashlib import sha256
from random import shuffle

secret = b'SSS Rulz!'
h_secret = sha256(secret).digest().hex().encode()
chunks = [h_secret[:16], h_secret[16:32], h_secret[32:48], h_secret[48:]]

with open('../flag', 'wb') as f:
    f.write(b'SSS{' + b'\x80\x80\x80'.join(chunks) + b'}')

shuffle(chunks)

with open('../public/flag', 'wb') as f:
    f.write(b'SSS{' + b'\x80\x80\x80'.join(chunks) + b'}')

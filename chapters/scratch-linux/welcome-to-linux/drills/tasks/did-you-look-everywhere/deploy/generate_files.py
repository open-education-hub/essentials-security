#! /bin/bash

from os import makedirs
from random import choice
import string

DIRECTORIES = [
    '/home/ctf/south-park/randy/tegridy',
    '/home/ctf/south-park/randy/pangolin',
    '/home/ctf/south-park/randy/lorde',

    '/home/ctf/south-park/al-gore/manbearpig',

    '/home/ctf/south-park/token/tolkien',
    '/home/ctf/south-park/token/tupperware',

    '/home/ctf/south-park/timmy/timmeh',

    '/home/ctf/south-park/cartman/respect-my-authoritah',
    '/home/ctf/south-park/cartman/cartmenez',
    '/home/ctf/south-park/cartman/scott-tenorman'
]

CHARSET = string.ascii_letters + string.digits + '_'
FLAG_LEN = len(open('/home/ctf/flag').read())

def randStr(length=10):
	return ''.join(choice(CHARSET) for _ in range(length))

for directory in DIRECTORIES:
    makedirs(directory, 0o755)
    for _ in range(10):
        with open(f'{directory}/{randStr()}', 'w') as f:
            f.write(randStr(FLAG_LEN - 1) + '\n')

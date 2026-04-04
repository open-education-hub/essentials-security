#! /usr/bin/python

from hashlib import sha256
from os.path import join

files_flags = {
    'terminal': 'btw_i_use_arch',
    'root': 'born_to_be_root',
    'find': 'you_finally_found_me',
    'grep': 'not_here_either',
    'file': 'why_keep_looking',
    'strings': 'you_ve_already_found_the_answer',
    '.hidden': 'sneaky_sneaky',
    'admin': 'ew_windows',
    '9': 'u_wot_m8',
    '10': 'what_are_you_doing_here',
}

for file, flag in files_flags.items():
    enc_flag = sha256(flag.encode()).digest().hex()
    file_path = join('..', 'public', 'flags', file)
    open(file_path, 'w').write(f'SSS{{{enc_flag}}}\n')

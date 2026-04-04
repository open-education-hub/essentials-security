import requests

local = True
PORT = 8010

if local:
    URL = f'http://localhost:{PORT}/one-by-one'
else:
    URL = f'http://141.85.224.102:{PORT}/one-by-one'

s = requests.Session()

last_chr = ''
flag = ''

while last_chr != '}':
    r = s.get(URL)
    last_chr = r.text[3]
    flag += last_chr

print(flag)

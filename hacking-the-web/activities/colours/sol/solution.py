import requests as re

PORT = 8016
local = True

if local:
    URL = f'http://localhost:{PORT}/colours/index.php'
else:
    URL = f'http://141.85.224.102:{PORT}/colours/index.php'

for i in range(10000):
    resp = re.get(f'{URL}?index={i}')
    if 'SSS' in resp.text:
        print(f'index = {i}')
        print(resp.text)
        break

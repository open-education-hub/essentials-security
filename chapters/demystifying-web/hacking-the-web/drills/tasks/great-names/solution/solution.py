import requests

PORT = 8014
local = True

if local:
    URL = f'http://localhost:{PORT}'
else:
    URL = f'http://141.85.224.102:{PORT}'

s = requests.Session()

s.get(URL)
s.cookies.set('christopher', 'columbus')

resp = s.get(URL)
print(resp.text)

import requests

PORT = 8012
local = True

if local:
    URL = f'http://localhost:{PORT}/human-asimov.php'
else:
    URL = f'http://141.85.224.102:{PORT}/human-asimov.php'

s = requests.Session()
s.cookies.set('robotType', 'ASIMOV')

resp = s.get(URL)
print(resp.text)

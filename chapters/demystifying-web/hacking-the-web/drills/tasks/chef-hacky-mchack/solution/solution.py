import requests

PORT = 8013
local = True

if local:
    URL = f'http://localhost:{PORT}/manage.php'
else:
    URL = f'http://141.85.224.102:{PORT}/manage.php'

s = requests.Session()
s.cookies.set('u', 'hacky mchack')

resp = s.get(URL)
print(resp.text)

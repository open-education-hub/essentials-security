import requests

local = True
PORT = 8011

if local:
    URL = f'http://localhost:{PORT}/produce-consume'
else:
    URL = f'http://141.85.224.102:{PORT}/produce-consume'

s = requests.Session()

s.get(f'{URL}/produce.php')
resp = s.get(f'{URL}/consume.php')

print(resp.text)  # TODO; only print flag

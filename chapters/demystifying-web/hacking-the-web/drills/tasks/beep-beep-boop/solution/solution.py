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
    URL = f"http://localhost:{PORT}/human-asimov.php"
else:
    URL = f"http://{HOST}:{PORT}/human-asimov.php"

s = requests.Session()
s.cookies.set("robotType", "ASIMOV")

resp = s.get(URL)
print(resp.text)

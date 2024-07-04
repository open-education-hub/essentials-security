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
    URL = f"http://localhost:{PORT}/one-by-one"
else:
    URL = f"http://{HOST}:{PORT}/one-by-one"

s = requests.Session()

last_chr = ""
flag = ""

while last_chr != "}":
    r = s.get(URL)
    last_chr = r.text[3]
    flag += last_chr

print(flag)

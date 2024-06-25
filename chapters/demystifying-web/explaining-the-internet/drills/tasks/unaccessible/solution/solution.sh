#! /bin/bash
# SPDX-License-Identifier: BSD-3-Clause

JOHN_PATH="$HOME/john/run"

rm -f "$JOHN_PATH"/john.pot

pass=$("$JOHN_PATH"/john ../public/password.txt \
  --format=Raw-MD5 \
  --wordlist="$JOHN_PATH"/password.lst | \
  grep stupid | \
  tr -s ' ' | \
  tr -d '\(\)' | \
  cut -d ' ' -f2)

echo -e "\nPassword is: $pass"

ssh vuln@141.85.224.70 -p 33222

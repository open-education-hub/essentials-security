#! /bin/bash

PORT=8012

if [[ $1 == "local" ]]; then
    URL="http://localhost:$PORT/human-asimov.php"
else
    URL="http://141.85.224.102:$PORT/human-asimov.php"
fi

curl -b 'robotType=ASIMOV' $URL

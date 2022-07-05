#! /bin/bash

PORT=8014
COOKIE_FILE=cookies.txt

if [[ $1 == "local" ]]; then
    URL="http://localhost:$PORT/"
else
    URL="http://141.85.224.102:$PORT/"
fi

curl -c $COOKIE_FILE $URL

curl -b $COOKIE_FILE -b "christopher=columbus" $URL

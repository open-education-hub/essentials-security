#! /bin/bash

PORT=8013

if [[ $1 == "local" ]]; then
    URL="http://localhost:$PORT/manage.php"
else
    URL="http://141.85.224.102:$PORT/manage.php"
fi

curl -b 'u=hacky mchack' $URL

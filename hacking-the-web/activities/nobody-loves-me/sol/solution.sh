#! /bin/bash

PORT=8017

if [[ $1 == "local" ]]; then
    URL="http://localhost:$PORT/nobody-loves-me/ernq-svyr.php"
else
    URL="http://141.85.224.102:$PORT/nobody-loves-me/ernq-svyr.php"
fi

curl -s $URL

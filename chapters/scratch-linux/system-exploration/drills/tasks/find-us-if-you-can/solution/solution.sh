#! /bin/bash

echo "Get the first flag."
# Use 2> /dev/null to ignore the error messages.
find / -type f -name flag 2> /dev/null | xargs cat | grep SSS

echo "Now get the second one."
find / -name *doc* 2> /dev/null | grep bugs | xargs cat

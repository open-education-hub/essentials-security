#! /bin/bash
# SPDX-License-Identifier: BSD-3-Clause

echo "Get the first flag."
# Use 2> /dev/null to ignore the error messages.
find / -type f -name flag -print0 2> /dev/null | xargs -0 cat | grep SSS

echo "Now get the second one."
find / -name '*doc*' -print0 2> /dev/null | grep --null-data bugs | xargs -0 cat

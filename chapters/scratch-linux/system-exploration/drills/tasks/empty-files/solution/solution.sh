#! /bin/bash

find /home/ctf/south-park/ -type f -size +0c | sort -t '/' -k4 | xargs cat

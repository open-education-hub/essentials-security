#! /bin/bash

find /home/ctf -size +1c | sort | xargs cat | tr -d "\n"

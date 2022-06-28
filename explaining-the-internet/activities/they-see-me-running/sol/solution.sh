#! /bin/bash

echo -e "1\nTCP" | nc localhost 31337 | grep SSS
echo -e "2\n32" | nc localhost 31337 | grep SSS
echo -e "3\n3" | nc localhost 31337 | grep SSS
echo -e "4\nessentials/explaining-the-internet" | nc localhost 31337 | grep SSS
echo -e "5\nUDP" | nc localhost 31337 | grep SSS

# Pinger: Solution

## Vulnerability

The `ping` server calls `subprocess.Popen('ping -c 1 ' + user_input)`.
This leaves it vulnerable to a command injection attack.

## Exploit

First do some recon and use `; ls` to explore the remote system.
If you do it well, you'll find the flag in `/home/ctf`.
Now use `; cat /home/ctf/flag` to read it.

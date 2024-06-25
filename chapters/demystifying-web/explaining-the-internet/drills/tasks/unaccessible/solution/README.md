# Unaccessible: Solution

## Vulnerability

The server's password is weak (`stupid`) and is included in `john`'s wordlist(`password.lst`).

## Exploit

Use `john` to find the password using its default wordlist.
Then use this password to `ssh` into the container and read the flag from `/home/ctf`

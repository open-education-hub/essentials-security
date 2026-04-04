# Empty Files: Solution

Most files truly are empty, but not *all* of them.
Use `find` to list the non-empty ones:
```
$ find /home/ctf/south-park -size +0c
```

This reveals a smaller amount of files.
The flag is made up of all of these files concatenated.
```
$ find /home/ctf/south-park -size +0c | xargs cat
```

Now the characters are not in the correct order, however:
- three files contain `S` characters
- one file contains `{` and another one contains `}`

Probably each file contains one letter of the flag.
The correct ordering is given by sorting the files lexicographically.
For this, we'll use the `sort` command before `cat`-ting the files.
```
$ find . -type f -size +0c | sort -t '/' -k4 | xargs cat
```

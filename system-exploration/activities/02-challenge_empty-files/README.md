# Empty Files

## Description

The `/home/ctf` folder houses a large hierarchy of files.
Most of them are empty.

## Solution

Most files truly are empty, but not *all* of them.
Let's find the non-empty ones, using `find`:
```
# find /home/ctf -size +1c
```

This reveals a smaller amount of files.
Inspecting them reveals that each contains exactly one character.
But what's more interesting is that exactly 3 files contain capital `S`'s, some contain `_` characters, one contains a `{`, another one a `}` and the rest contain various lowercase characters.
It looks like our flag is made up of all of these files concatenated.
So let's concatenate them!
```
# find /home/ctf -size +1c | xargs cat
```

Oh... it seems the characters are not in the correct order...
But wait a second:
- the file `002` contains the string `S`;
- the file `004` contains the string `S`;
- the file `005` contains the string `S`;
- the file `008` contains the string `{`;
- the file `969` contains the string `}`.

It may be that the correct ordering is given by sorting the files lexicographically.
For this, we'll use the `sort` command before `cat`-ting the files.
```
# find /home/ctf -size +1c | sort | xargs cat
```

A nice trick so the flag appears on a single line is to delete the `\n` characters.
You can do this via the `tr` command.
Feel free to consult its `man` page for details.
The resulting command, which you can see in the [solution script](./sol/solution.sh), is called a **oneliner**.
Oneliners make you look like a true hacker.

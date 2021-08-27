# Find Us If You Can

## Description

This challenge has you look for two flags.
Once found, the first flag gives you a hint about how to find the second flag.

## Solution

We assume the first flag's name is simply `flag`.
Thus, we use `find` to search for any files with this name:
```
# find / -type f -name flag
/proc/1/net/stat/flag
```
So the flag is in `/proc/1/net/stat`... of all places.
Now we read it:
```
# cat /proc/1/net/stat/flag
```

Most likely, the "What's up, doc?" part is our hint, but what does it mean?
The Bugs Bunny reference is obvious, but how can we use it?

How about we look for files containing the word `doc`?
```
# find / -name *doc*
```
The command yields too many results.
We need to trim them.
`grep` time!

Let's try to `grep` the word `bugs`:
```
# find / -name *doc* | grep bugs
/tmp/.hidden/my/bugs/bunny/bugs_bunny.doc
# cat /tmp/.hidden/my/bugs/bunny/bugs_bunny.doc
```

# Find Us If You Can: Solution

We assume the first flag's name is simply `flag`.
Thus, we use `find` to search for any files with this name:
```
$ find / -type f -name flag
/proc/1/net/stat/flag
```
So the flag is in `/proc/1/net/stat`.
Now we read it:
```
$ cat /proc/1/net/stat/flag
```

The `"What's up, doc?"` part is our hint.
We should look for files containing the word `doc`:
```
$ find / -name *doc*
```
The command yields too many results.
We need to trim them, by `grep`ping for `bugs`:
```
$ find / -name *doc* | grep bugs
/tmp/.hidden/my/bugs/bunny/bugs_bunny.doc
$ cat /tmp/.hidden/my/bugs/bunny/bugs_bunny.doc
```
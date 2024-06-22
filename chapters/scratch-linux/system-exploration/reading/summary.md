# Summary

Here are a few useful snippets from today's session:

- `grep -R "some string" /some/path`: recursively looks for "some string" inside all the files in the `some/path` directory;
- `find /some/path -name *flag* -type f`: recursively searches for regular files in the `/some/path` directory, whose names include the word `flag`;
- `cat large_file | grep SSS`: looks for the `SSS` string in a large file, so you don't have to do this manually;
- `find some/path <some criteria> | xargs grep SSS`: look for the `SSS` string in each file that matches some specified criteria.

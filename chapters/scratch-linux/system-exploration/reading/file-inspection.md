# Inspecting Files

Now that we can find our way inside a file hierarchy, we need a means by which to inspect those files.
`grep` works just fine, provided we're dealing with text files.
But what if we aren't?

In this case, we'll need to take a sneak peak into some _binary analysis_.
We'll get back to this subject starting from Session [Data Representation](../data-representation).

## `file`

First, we want to get some more detailed information about what type of binary file we are dealing with specifically.
`ls` already gives us information such as the file's name, size and permissions.
This is all fine, but this information is common to all files.
Whether we're dealing with an image, or with an executable file `ls` won't tell us.

But `file` does.
`file` works by reading a file's header (the first few bytes at the beginning of the file, which hold information about its format and type).
Thus, it is capable of outputting more precise information than `ls`.
Let's test it using one of today's challenges, `drills/tasks/not-your-doge/support/not-doge.pnm`.

```bash
root@kali:~/essentials-security/chapters/scratch-linux/system-exploration# file drills/tasks/not-your-doge/support/not-doge.pnm
drills/tasks/not-your-doge/support/not-doge.pnm: Netpbm image data, size = 500 x 590, rawbits, pixmap
```

## `strings`

One of the most basic forms of binary analysis is to simply look for any human-readable string present in a binary file.
For this purpose, we'll use the `strings` command.

# Ghidra Killer Solution

As the name says, `Ghidra` will crash if used on the binary.
`Strings` is useless, because the binary reads the flag from a file.
`GDB` is also useless (and will also crash).
The only way is to use `strace`, to see what the program actually does.

We can see an `openat()` call, which gives us the path to the flag.

```shell
openat(AT_FDCWD, "flag", O_RDONLY)
```

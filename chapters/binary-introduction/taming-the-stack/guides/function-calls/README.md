# Function Calls

Use `objdump` to investigate the prologue of the `read_array()` and `print_array()` functions.

```console
root@kali:~$ objdump -d -M intel main
```

Notice how in the prologue, `ebp` saves the `esp` value before the local variables are stored on stack:

```asm
080491a6 <read_array>:
 80491a6:       55                      push   ebp
 80491a7:       89 e5                   mov    ebp,esp
 80491a9:       83 ec 18                sub    esp,0x18
 80491ac:       83 ec 08                sub    esp,0x8
```

What's more, take a closer look at how the parameters are handled:

```asm
 80491af:       ff 75 0c                push   DWORD PTR [ebp+0xc] ; the second argument of read_array()
 80491b2:       68 08 a0 04 08          push   0x804a008
 80491b7:       e8 c4 fe ff ff          call   8049080 <__isoc99_scanf@plt>

 8049213:       8b 45 08                mov    eax,DWORD PTR [ebp+0x8] ; the first argument of print_array()
```

Now, inside `gdb`, let's take a look at where the return address is saved:

```console
pwndbg> info frame
Stack level 0, frame at 0xffffcd30:
 eip = 0x80491ac in read_array (main.c:5); saved eip = 0x8049273
 Saved registers:
  ebp at 0xffffcd28, eip at 0xffffcd2c

pwndbg> x 0xffffcd2c
0xffffcd2c:     0x08049273
```

Let's do the math:

- `ebp` points at `0xffffcd28`
- `ebp + 4` will then point at `0xffffcd2c`
- the value stored at `0xffffcd2c` is `0x08049273`, the same as the one from the saved `eip`

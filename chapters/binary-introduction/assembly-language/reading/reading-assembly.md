# Reading Assembly

## `objdump`

Starting from an executable file, we can read its Assembly code by **disassembling** it.
The standard tool for doing this is `objdump`:

```console
root@kali:~$ objdump -M intel -d <binary> | less
```

- Use `-M intel` for Intel syntax.
The default syntax is AT&T.
- `-d` stands for "disassembly".
- pipe the output to `less` so you can navigate the Assembly code more easily.

Notice that every line contains an address, an opcode and an instruction.
The opcode is simply the binary representation of that instruction.

Alternatively, you can use GDB and Ghidra that you learned about [in the previous session](../../Binary%20Analysis/).

## GDB

The undisputed king of Assembly is by far the **GNU DeBugger (GDB)**.
It's just what its name says it is, but its beauty is in its versatility.
GDB is a command-line debugger that allows us to print registers, variables, dump memory from any address, step through the code, go back through the call stack and much more.
Today we will only get a glimpse of its power.

We are using the `pwndbg` extension for GDB as it allows us to view the assembly code, stack (you'll learn about it in the [next session](../../Taming%20the%20Stack/)) and registers.
Follow the instructions [here](https://github.com/pwndbg/pwndbg#how) to install it if you haven't done so already.

GDB can run Assembly instructions one by one and stops after each instruction.
The current instruction is also clearly displayed.
Below is a reduced list of useful GDB commands to get you going.
Use it as a cheatsheet when you get stuck:

- `start` = start running the program from `main`
- `list` = decompile and display C code
Only works for executables compiled with `-g`
- `pdis` = disassemble and display instructions with nice syntax highlighting
- `next` / `n` = run the current C code
If it is a function call, it is executed without stepping into the function.
- `nexti` / `ni` = run the current Assembly instruction
- `step` / `s` = if the debugger has reached a function call, step into it.
Otherwise, it behaves like `next` / `n`
- `stepi` / `si` = step into function (used for the `call` instruction in Assembly)

- `break` / `b <n>` = place a breakpoint at line `n`
- `break` / `b *<address>` = place breakpoint at address
- `continue` / `c` = run code until next breakpoint
- `info registers <name>` = display the values in all registers.
If a name is specified, only the value in that register is displayed
- `p <variable>` / `<name>` = print the variable / number; similar to `printf`

```console
p/d = printf("%d")
p/c = printf("%c")
p/x = printf(“%x”)
p/u = printf(“%u”)
```

- `x <address>` = print data at the address (dereference it).
By default, the output is represented in hex
- `x/<n><d><f> <address>` -> print `n` memory areas of size `d` with format `f`:

```console
n = any number; default = 1
d = b (byte - default) / h (half-word = short) / w (word = int)
f = (like p): x (hex - default)  / c (char) / d (int, decimal) / u (unsigned)  / s (string)
```

Examples:

```console
x/20wx = 20 hex words (ints)
x/10hd = 10 decimal half-words (shorts)
x/10c = 10 ASCII characters
x/10b = 10 hex bytes (because x is the default)
```

- `set $<register> <value>` = sets the register to that value

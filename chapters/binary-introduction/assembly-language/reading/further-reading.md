# Further Reading

## The Whole ISA

If you want to search for an instruction, use [this](https://www.felixcloutier.com/x86/) website.
Each instruction has its own table with all possible operands and what they do.
Note that `imm8` means "8-bit immediate" (an 8-byte regular number), `imm64` means a 64-bit immediate and so on.
Similarly, `reg32` means a 32-bit register and `m16` for example means a 16-bit (2-byte) memory area.
You'll see `reg`, `imm` and `m` combined with `8`, `16`, `32` and `64` depending on what each instruction does.

## Caches

Many programs access the same addresses repeatedly over a short period of time.
Take a short 1000-step loop.
It uses the same code 1000 times.
It would be inefficient for the CPU to read the instructions directly from the RAM 1000 times.
For this reason, there is an intermediary level of memory between the RAM and the registers, called **the cache**.

As their name implies, caches store the contents of some memory addresses that are frequently requested by the CPU.
We say _caches_, in plural because they are laid out hierarchically, each lower level being faster and smaller than the ones below.
Usually, CPUs have 3 levels of cache memory.
You can query their sizes with the `lscpu` command:

```console
root@kali:~$ lscpu
[...]
L1d cache:                       128 KiB
L1i cache:                       128 KiB
L2 cache:                        1 MiB
L3 cache:                        6 MiB
[...]
```

Notice the L1 (level 1) cache is split between a data cache (`L1d`) and an instruction cache `L1i`.
The other caches do not store data and instructions separately.

## Assembly Syntaxes

This session we've used the Intel syntax for writing and displaying Assembly.
We did so because it's more straightforward than its alternative: the AT&T syntax.
You can find the differences on [Wikipedia](https://en.wikipedia.org/wiki/X86_assembly_language#Syntax).

## `lea`

`lea` stands for "Load Effective Address".
Its syntax is:

```asm
lea dest, [address]
```

It loads `address` into the `dest` register (it can only be a register).
What's interesting about it is that it also uses the `[...]` syntax, but **does not dereference the address**.
In the snippet below, `0xdeadbeef` is simply copied to `rax`.

```asm
lea rax, [0xdeadbeef]
```

Its true power comes from the fact that it can also compute an address.
For example, the code below will first compute the address given by `rdi + rcx * 8 + 7` and then write this address into `rax`.

```asm
lea rax, [rdi + rcx * 8 + 7]
```

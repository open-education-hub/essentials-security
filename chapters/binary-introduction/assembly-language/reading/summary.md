# Summary

The key takeaways from this session are:

- Assembly is a human-readable representation of instructions executed by the CPU
- It allows us to access CPU registers directly
- It uses a fixed set of instructions called ISA
- **Memory** is the RAM, **storage** is the disk
- Data is stored in memory using the little endian representation
- You can disassemble a program with `objdump` like so:

```console
root@kali:~$ objdump -M intel -d <program> |less
```

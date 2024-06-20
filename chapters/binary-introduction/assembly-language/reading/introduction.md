# Introduction

In the previous 2 sessions you started discovering what binary security looks like.
[Last session](../../Binary%20Analysis/) you learnt two very powerful means of investigating and even reverse engineering executables: static and dynamic analysis.
In order to leverage them efficiently, you used Ghidra for static analysis.
Now we'll introduce GDB for dynamic analysis.
You've most likely noticed that they are able to display the source code of the application.
GDB can do so when said app was compiled with _debug symbols_, while Ghidra does not even need debug symbols.
It infers the original C code from its compiled representation (learn more about how Ghidra does this by taking part in the [Binary Security track](https://security-summer-school.github.io/binary/static-analysis/#ida-and-ghidra) next year).
This representation is called **assembly language**.
Both Ghidra and GDB can display the program's code in assembly language.
Today we will demystify this low-level language and learn to understand it.

## Reminders and Prerequisites

For this session, you need:

- a working knowledge of the C programming language and familiarity with pointers
- basic skills with Ghidra and GDB
- understand how an executable file is created, as described in the [Application Lifetime session](../../Application%20Lifetime)
- knowledge of the following means of representing data: ASCII, binary, hexadecimal.

Check out the session on [Data Representation](../../../Data/Data%20Representation/) for a reminder.

## Assembly

Assembly is a low-level language used as a human-readable representation of instructions executed by the CPU.
There is a one-to-one mapping between the binary code executed by the CPU and Assembly.
Few people write Assembly, but many people are required to read it:

- security engineers
- compiler / interpreter developers
- embedded developers
- operating systems developers

Simply put, if a field is close to CPU it requires (some knowledge of) Assembly.
So let's learn this language!

# Dynamic Analysis

Dynamic analysis means observing the behaviour of the binary, while it is running.
This is performed by tracing or sandboxing.

Tracing is the process during which various checkpoints are placed in the code, that send alerts when the execution has reached them.
Generally, the context (registers, stack, variables) is also displayed.

Sandboxing is a more complex process, in which you isolate a binary in a virtual machine (usually), run it and observe the changes made on the system: modified files, network traffic, etc.

Today, we are going to explore tracing.

## strace

`strace` shows system calls performed by a binary application.
That means opening any kind of file, reading and writing into files, `mprotect`s and other things.
It is useful to find out if the program does any changes to the system itself, or if it writes in some files.

## ltrace

`ltrace` shows calls to dynamic library functions, along with system calls.
It is similar to `strace`.

## gdb

GDB is the most powerful dynamic analysis tool available to the regular user.
It allows executing the code instruction by instruction, inspecting memory areas, changing memory areas, jumping to other pieces of code, that weren't executed normally.
GDB is best used when the user has knowledge about assembly language, which will be presented in the last 2 sessions.
For this session, GDB isn't required.

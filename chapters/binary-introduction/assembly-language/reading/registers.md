# Registers

You might have already seen the image below.
It shows the various places where data can be kept.
Note that this data can be both non-persistent and persistent.
Non-persistent data is gone once you shut down the computer.
It's kept in all levels from "Main Memory" upwards.
The "Main Memory" is simply referred to as **memory** or RAM.

Persistent storage refers to data on **disks**: HDD, SSD, CDs, DVDs, magnetic tapes, even in the cloud (where cloud storage providers also use HDDs, SSDs etc.).
If you shut down your laptop or your mobile phone, your pictures or video games remain unchanged.
This is because they are stored _on your device's disk_.
We simply refer to persistent storage as **storage**.
Take note of the difference between _storage_ and _memory_.

![Memory Hierarchy](../media/memory-hierarchy.png)

In most programming languages you can freely access data everywhere up to and including the memory.
In assembly however, you also have access to the **registers** and can influence the **cache**.
We won't be dealing with the cache in this session, but you can read more about them [here](further-reading.md#caches)
They are the fastest form of memory available and are implemented **inside the CPU**.
We can access data in registers in less than 1 ns (nanoseconds), as opposed to a few dozen ns when fetching data from the RAM.

Then why not make more registers and only use them instead of RAM?
Registers are fast because they are few in number.
This allows them to be efficiently wired to the CPU's Arithmetic and Logic Unit (ALU), which is responsible for executing basic operations, such as addition, subtraction, bitwise and, or, shifts etc.
The more registers, the more complex and the less efficient the logic.

## Registers in an X64 CPU

Registers are like variables with fixed names embedded in the CPU.
They can be assigned values that can be modified via instructions.
There are several types of registers inside a CPU.
All of them can be assigned data and that data can be modified using the assembly-level operations described [further in this session](assembly-instructions.md).

All registers are **64-bits** wide.
So they each can store up to 8 bytes of data.

### `rip`

We'll start with a very special and illusive one: the **instruction pointer** - `rip`.
In [the previous session](../../Binary%20Analysis/), you learned that the code of any process is also in its memory.
In order to read and execute it, the CPU must "follow" it just like children follow text with their fingers.
The CPU does this using `rip`.
This register stores te **address of the currently executed instruction**.
We will never use this instruction per-se in instructions, but you will see and make use of it in GDB.

### General Purpose Registers

Then there are **general purpose registers**.
As their name implies, they are used to store _anything_: addresses, user input, function parameters, data read from files or from the web etc.
Some of them also have some special functions, especially regarding function calls:

- `rax`: accumulator register
- `rbx`: base register
- `rcx`: counter register; used with the [`loop`](assembly-instructions.md#loops) instruction
- `rdx`: data register
- `rdi`: destination register
- `Rsi`: source register
- `r8`, `r9` ... `r15`: regular registers

Do not learn them by heart.
And also do not bother with their extra meanings.
We will make use of those only when specified.
Otherwise, treat them as simple variables.

### Smaller Registers

Sometimes you only need to access 32 or 16 or 8 bits out of a 64-bit register.
This is possible by slightly changing the name of the register like so:

| 64 bits | Lowe 32 bits | Lower 16 bits | High 8 bits  | Low 8 bits |
|:-------:|:------------:|:-------------:|:------------:|:----------:|
| `rax`   | `eax`        | `ax`          | `ah`         | `al`       |
| `rdi`   | `edi`        | `di`          | inaccessible | `dil`      |
| `r8`    | `r8d`        | `r8w`         | inaccessible | `r8l`      |

The bits contained in each of the above subdivisions are shown in the image below.
It is similar for `rdi` and `r8`, it's just the names that differ.

![rax Subdivisions](../media/rax-subdivisions.svg)

`rbx`, `rcx` and `rdx` have the same subdivisions as `rax`.
`rsi` has the same subdivision as `rdi`: `esi`, `si` and `sil`.
It doesn't make sense to access 4 bytes of an address.
The lower 2 bytes can be accessed due to historical reasons.
In the 70s, when the first CPU of this family (8086) was launched, it only supported 2-byte addresses.
All registers `r9` to `r15` have the same subdivisions as `r8`.

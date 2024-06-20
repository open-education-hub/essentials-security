# Assembly Instructions

We've now learned what assembly is theoretically and what registers are, but how do we use them?
Each CPU exposes an **ISA (Instruction Set Architecture)**: a set of instructions with which to modify and interact with its registers and with the RAM.
There are over 1000 instructions in the x64 ISA.
There are even instructions for efficiently encrypting data.
Find out more about them by enrolling in the [Hardware Assisted Security track](https://github.com/security-summer-school/hardware-sec/).

Before we dive into the instructions themselves, it's useful to first look at their generic syntax:

```asm
instruction_name destination, source
```

Most Assembly instructions have 2 operands: a source and a destination.
For some operations, such as arithmetic, the destination is also an operand.
The result of each instruction is always stored in the destination.

Below we'll list some fundamental instructions.
We will be using the Intel Assembly syntax.

## `mov`

`mov` is the most basic instruction in Assembly.
It _copies_ (or _moves_) data from the source to the destination.
Also note that comments in Assembly are preceded by `;` and that the language is case-insensitive.

```asm
mov eax, 3              ; eax = 3

mov rbx, "SSS Rulz"     ; place the string "SSS Rulz" in `rbx`
; This places each byte of the string "SSS Rulz" in rbx.

mov r8b, bh             ; r8b = bh
; The sizes of the operands must be equal (1 byte each in this case).
```

## Data Manipulation

Now that we've learnt how to place data in registers we need to learn how to do math with it.
As you've seen so far, Assembly instructions are really simple.
Below is a table with the most common and useful arithmetic instructions.
Try to figure out what each example does.
Use the fact that the general anatomy of an instruction is usually `instruction destination, source`.
The result is always stored in the `destination`

| Instruction          | Description     | Examples                          |
|:--------------------:|:---------------:|:---------------------------------:|
| `add <dest>, <src>`  | `dest += src`   | `add rbx, 5`<br/>`add r11, 0x99`   |
| `sub <dest>, <src>`  | `dest -= src`   | `sub ecx, 'a'`<br/>`sub r9, r8`    |
| `shl <dest>, <bits>` | `dest <<= bits` | `shl rax, 3`<br/>`shl rdi, cl`     |
| `shr <dest>, <bits>` | `dest >>= bits` | `shr r15, 5`<br/>`shr rsi, cl`     |
| `and <dest> <src>`   | `dest &= src`   | `and al, ah`<br/>`and bx, 13`      |
| `or <dest> <src>`    | `dest \|= src`  | `or r10b, cl`<br/>`or r14, 0x2000` |
| `xor <dest> <src>`   | `dest ^= src`   | `xor ebx, edx`<br/>`xor rcx, 1`    |
| `inc <dest>`         | `dest++`        | `inc rsi`                         |
| `dec <dest>`         | `dest--`        | `dec r10w`                        |

## Control Flow

Now we know how to do maths and move bits around.
This is all good, but we still can't write full programs.
We need a mechanism similar to `if`s from Python and also loops in order to make the code run based on conditions.

### `jmp`

The simplest instruction for control flow is the `jmp` instruction.
It simply loads an address into the `rip` register.
But when Assembly code is generated or written either by the compiler or by us, instructions don't have addresses yet.
These addresses are assigned during the **linking** or **loading** phase, as you know from the [Application Lifetime session](../../Application%20Lifetime/).

For this reason, we use **labels** as some sort of anchors.
We `jmp` to them and then the assembler will replace them with relative addresses which are then replaced with full addresses during linking.
The way in which `jmp` and labels function is very simple.
Remember that in the absence of `jmp`s, Assembly code is executed linearly just like a script.

```asm
    jmp skip_next_section

    ; Whatever code is here is never executed.

skip_next_section:
    ; Only the code below this label is executed.
```

> **Warning**
> Do not confuse labels with functions.
> A label does not stop the execution of code when it's reached.
> They are simply ignored by anything except for `jmp`.

For example, in the following code, both instructions are executed in the absence of `jmp`s:

```asm
    mov rax, 2
some_label:
    mov rbx, 3
    ; rax = 2; rbx = 3
```

### `eflags`

Each instruction (except for `mov`) changes the **inner state of the CPU**.
In other words, several aspects regarding the result of the instruction are stored in a special register that we cannot access directly, called `eflags`.
There are [instructions](https://stackoverflow.com/questions/1406783/how-to-read-and-write-x86-flags-registers-directly) that can set or clear some flags in `eflags`, but we cannot write something like `mov eflags, 2`.

As its name implies, each bit in `eflags` is a flag that is activated (i.e. set to 1) if a certain condition is true about the result of the last executed instruction.
We won't be using these flags per se with one exception: `ZF` - the **zero flag**.
When active, it means that the result of the last instruction was... 0, duh!
This is useful for testing if numbers are equal for example.
We'll talk about this in the next section.

### Conditional jumps

Now we know that there is an internal state of the CPU which is modified by each instruction, except for `mov`.
We still need a way to leverage this state.
We can do this via **conditional jumps**.

They are like `jmp` instructions, but the jump is made only when certain conditions are met.
Otherwise, code execution continues from the next instruction.
The general syntax of a conditional jump is

```asm
j[n]<cond> label
```

where the letter `n` is optional and means the jump will be made if the condition is **not** met.

#### `cmp` and `test`

We can use the regular arithmetic instructions that we've learned so far to modify `eflags`.
But this has the drawback of also modifying our data.
It would be great if we had a means to modify `eflags` without changing the data that we evaluate.
We can do this using `cmp` and `test`.

`cmp dest, src` modifies `eflags` as if you were **subtracting** `src` from `dst`, but without modifying `dst`.
This is great for testing if 2 things are equal, or for testing which is greater or lower.

`test dest, src` is similar to `cmp`, but modifies `eflags` according to the `and` instruction.
This comes in handy when we want to check if a register is 0.

```asm
test rax, rax
jz rax_is_zero
```

is equivalent to

```asm
cmp rax, 0
jz rax_is_zero
```

Now let's have a look at some conditional jumps:

| Conditional jump           | Meaning                                                       |
|:--------------------------:|:-------------------------------------------------------------:|
| `jz` / `je`                | Jump if the Zero Flag is active                               |
| `jnz` / `jne`              | Jump if the Zero Flag is not active                           |
| `cmp rax, rbx`<br/>`j[n]g`  | Jump if `rax` is (not) greater (signed) than `rbx`            |
| `cmp rax, rbx`<br/>`j[n]a`  | Jump if `rax` is (not) greater (unsigned) than `rbx`          |
| `cmp rax, rbx`<br/>`j[n]ge` | Jump if `rax` is (not) greater (signed) or equal than `rbx`   |
| `cmp rax, rbx`<br/>`j[n]ae` | Jump if `rax` is (not) greater (unsigned) or equal than `rbx` |
| `cmp rax, rbx`<br/>`j[n]l`  | Jump if `rax` is (not) lower (signed) than `rbx`              |
| `cmp rax, rbx`<br/>`j[n]b`  | Jump if `rax` is (not) lower (unsigned) than `rbx`            |
| `cmp rax, rbx`<br/>`j[n]le` | Jump if `rax` is (not) lower (signed) or equal than `rbx`     |
| `cmp rax, rbx`<br/>`j[n]be` | Jump if `rax` is (not) lower (unsigned) or equal than `rbx`   |

### Loops

We can create loops simply by combining labels and conditional jumps.
For example, `for i in range(0, 10)` from Python is equivalent to:

```asm
    xor rcx, rcx    ; i = rcx; same as mov rcx, 0
for_loop:
    cmp rcx, 10
    je done_loop    ; verify i < 10

    ; The body of the for loop.

    inc rcx         ; rcx++
    jmp for_loop    ; re-evaluate the condition

done_loop:
```

Or alternatively, we can verify `rcx < 10` at the end of the loop:

```asm
    xor rcx, rcx
for_loop:
    ; The body of the for loop.

    inc rcx         ; rcx++
    cmp rcx, 10
    jb for_loop    ; verify i < 10

    ; The code here is executed only after the loop ends.
```

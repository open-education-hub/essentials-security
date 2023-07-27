# Functions and the Stack

Every function has two classes of values, usually stored on stack, extremely important for its well-being:

1. the return address

1. the parameters / arguments

Meddling with these might get you to a big fat **SEGFAULT** or to great power.

## `ebp`, the Stack Frame

But before discussing that, we have to bring light to another obscure register, `ebp`.
We kind of used it before, in our journey, as it has a great advantage.
It stores the stack pointer value right before the stack begins to hold local variables and preserved register values.
In other words, it keeps a pointer to the stack at the beginning of the function, enabling us to actually move freely through the stack.
We will, now, refer to values stored on it, even though they are not the last ones.

```asm
push ebp
mov ebp, esp

push dword 3
push dword 4
push dword 5

; at this point esp decreased its value with 3 * 4 = 12 bytes
; traditionally we can access the last value only,
; however the stack is like an array, so we will use the pointers
; it offers us

mov eax, [esp + 8] ; eax = 3
mov eax, [ebp - 4] ; eax = 3
```

## The Return Address

The return address of a function is one of the **most targeted** piece of information in an attack.
There is even a special class of attacks that takes its name from it, [ROP](https://security-summer-school.github.io/binary/return-oriented-programming/) (Return Oriented Programming).
Moreover, the return address can also be defined as a **code pointer**, a pointer that stores the address of an instruction.
Remember how the instructions were stored in the code or text section, hence the **code pointer** label.

The reason for this kind of popularity is obvious: it represents one of the rare instances when the program **performs a jump to a code pointer saved on stack**, which, combined with the stupidity or the laziness of the programmer, can result in a nasty backdoor to the system.

The address at which the return address is usually stored on x86 systems is `[ebp + 4]`.

## The Parameters

The parameters follow a similar story to that of the return address, with a slight modification, though.
On 64-bit x86 they are placed in special registers, if possible.
If the number of parameters is high, they would get transmitted using the stack, just as it happens, on 32-bit x86.

The address at which the first parameter gets stored on 32-bit x86 systems is `ebp + 8`.

The address at which the second parameter gets stored on 32-bit x86 systems is `ebp + 12`.

The address at which the third parameter gets stored on 32-bit x86 systems is `ebp + 16`.

And so on.

![parameters and ebp](../media/function-stack.jpg)

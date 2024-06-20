# Dereferencing Addresses

Up to this point we know how to operate with data and can write complex programs using conditional jumps.
But we know that data is stored mostly in the RAM.
How do we fetch it from there to our registers?

Imagine the RAM is one giant array.
Each byte is a cell in this array.
Therefore, each byte is found at a given **index** in this array.
Indices start at 0, so the first byte is found at index 0, the third 3 at index 2 and so on.
These indices are also called **memory addresses**, or simply **addresses**.

In order to load data from the RAM into our registers or vice-versa, we need to specify the CPU which RAM address to access.
This is called **dereferencing that address**.
Syntactically, this is very easy and is done by wrapping the address in `[]`.
The address can be either a raw number, or a register, or an expression:

```asm
mov rax, [0xdeadbeef]   ; load 8 bytes from the address 0xdeadbeef into rax
mov bx, [0xdeadbeef]    ; load 2 bytes from the address 0xdeadbeef into bx
mov [0xdeadbeef], ecx   ; store 4 bytes from ecx at the address 0xdeadbeef
```

Notice that the number of bytes that are transferred between the RAM and registers is given by the size of the register.
But what happens when we don't use a register?
The code below is incorrect because it is impossible to tell how many bytes to use to write 0x69.
We could write it using one byte of course, but what if we wanted to write it on 4 bytes and store `[ 0x00 | 0x00 | 0x00 | 0x69 ]`?
To eliminate such ambiguities, we must specify the number of bytes that we want to write to the RAM:

```asm
mov [0xdeadbeef], byte 0x2      ; writes 1 byte
mov [0xdeadbeef], word 0x2      ; writes 2 bytes: 0x00 and 0x02
mov [0xdeadbeef], dword 0x2     ; writes 4 bytes
mov [0xdeadbeef], qword 0x2     ; writes 8 bytes
```

Instead of a hardcoded value, we can express addresses as complex expressions which the CPU computes for us.
In the snippet below, the CPU computes the address given by `rdi + rcx * 4` and then writes the contents of `edx` there.

```asm
mov [rdi + rcx * 4], edx
```

This is equivalent to `v[i] = something` where `v` is an array of 4-byte values (hence `rcx * 4`):

- `rdi` = starting address of `v`
- `rcx` = `i`
- `edx` = `something`

Therefore, whenever you see `[...]` in Assembly, what between the square brackets is being dereferenced [**with one exception**](further-reading.md#lea).

## Endianness

This is all nice, but how does all this look like in the memory?
The order in which the bytes are stored in the RAM is called **endianness**.
Most CPUs store bytes **in reverse order**, or **little endian** order, because the least significant byte is the first.
When data is fetched back from the ram, the order is reversed:

```asm
mov [0x100], dword 0x12345678       ; the RAM at 0x100: [ 0x78 | 0x56 | 0x34 | 0x12 ]
mov ax, [0x100]     ; ax = 0x5678
mov bx, [101]       ; bx = 0x3456
```

However, endianness does not apply to strings.
The code below writes the string `SSS Rulz` at the address 0x100.
Notice we don't have to write it in reverse order like `zluR SSS`.

```asm
mov rax, "SSS Rulz"
mov [0x100], rax
; We need to use a register because mov cannot take both an address and a 64-bit immediate as operands.
; https://www.felixcloutier.com/x86/mov
```

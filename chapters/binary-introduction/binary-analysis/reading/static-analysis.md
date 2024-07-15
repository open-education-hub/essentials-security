# Static Analysis

Static analysis implies investigating the binary without running it.
This means looking into the effective binary file for strings, symbols, interesting addresses and so on.

## strings

`strings` is used to find strings in a binary file - very intuitive.
It is the most basic static analysis tool available.
Before any other more complex analysis takes place, a `strings` can find many hidden secrets.

## file

`file` is another useful tool, not only for binary analysis.
It should be used before any investigation, to make sure that the binary is a binary file, and not an archive.
It also shows if the executable is statically-linked (lots of strings, functions) or dynamically-linked.

### Counter-measures

For `file` there is no counter-measure to hide the data that would be found by it.
For `strings`, one way to counter it is to encrypt / obfuscate important data.
But keep in mind that the codified content will be visible, and can be deciphered.
That's why they are, almost always, used first when analysing a binary.

## nm

`nm` is used to find **symbols** - variable names, function names, and their addresses.
It also shows where these symbols are placed: text (T or t), rodata (R or r), bss (B or b), etc.
[Here](https://www.thegeekstuff.com/2012/03/linux-nm-command/) you can find all the symbols' meaning.

The difference between capital-letter symbols and lowercase symbols is the following:
Capital-letter symbols are global, meaning they can be referenced from other object files.
Example: `object1.o` has a global symbol named `global_var`.
`object2.o` can use `global_var`, if `object1.o` and `object2.o` are linked together.

### Counter-measures: Strip

`strip` removes all symbols from a binary file.
If a binary is stripped, `nm` becomes useless.

## objdump

`objdump` is a disassembler.
It takes binary files and transforms them to hexadecimal values and, where possible, assembly language.
It is useful in many cases: when we want to explore the sections of a program, when we want to see what a specific function does, or when we want to make sure that the binary won't crash more complex analysis tools (!).
`objdump` is a fast way to turn a binary file into more accessible format.

### Counter-measures

`objdump` is pretty good at what it must do.
It becomes less helpful if the binary is large, with multiple functions that call each other and we have a hard time understanding the flow of the application.
That's why it is a bad idea, generally, to break down real-life applications with `objdump`.

## Ghidra

`Ghidra` is a decompiler: it turns a binary file back into C code.
It also does function analysis, meaning it constructs a tree of function calls.
It is the best tool to understand what a binary does, without running it.

### Counter-measures

Unorthodox code, self-changing code, polymorphic code and other measures were taken by various people to counter Ghidra.
[This talk](https://www.youtube.com/watch?v=HlUe0TUHOIc&ab_channel=DEFCONConference) by Christopher Domas is one of the best examples of measures taken to counter Ghidra and other decompilers.

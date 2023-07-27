# Summary

The both curse and blessing of modern C/C++ code is the absolute control over memory it gives the programmer.
This comes as a doubled edged sword:

- the stack is just an array: we can modify and access it with `push` and `pop`, but also by using the special stack registers, `esp` and `ebp`
- direct access to the return address of the function at `ebp + 4`
- direct access to the parameters, found either in registers or on stack, at `ebp + 8`, `ebp + 12`, `ebp + 16` etc

making the program vulnerable to ROP attacks.

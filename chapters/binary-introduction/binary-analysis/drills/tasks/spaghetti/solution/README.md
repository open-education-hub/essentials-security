# Spaghetti Solution

The binary asks for a number.
After the number is provided, the program will call a function, depending on that number.
In this task, you must use `Ghidra` to follow the function-call graph, to find the right starting function, and then the number required.

`fn11()` is the target function.

The function call sequence, that ends with `fn11()` is the following:
`fn37()` -> `fn28()` -> `fn30()` -> `fn11()`.

`fn37()` is called by entering the `38` number.

# Quick Mafs

The flag's format is the classic `SSS{...}`, where `...` represent a string obtained by concatenating the **first 10 numbers** obtained by performing the computations below.

Let each number be `n[i]`, where `i` is its index.
`n[0] = 1337`.
This is your first number.
The next numbers are defined by the formula below, where `^` signifies exponentiation.

```text
n[i] = (n[i - 1]^3 * 67 + 31) % 2000, for all i > 0
```

And, please, don't compute the numbers manually.
You've just learned a cool new programming language that you can use!

If you're having difficulties solving this exercise, go through [this](../../../reading/enter-python.md) reading material.

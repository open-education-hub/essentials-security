# Enter Python

## The Basics

Python is a programming language designed with simplicity in mind.
It's meant to be simple and fast to read, understand and write.
This is evident even from the language's syntax.

To get accustomed to Python, take a look at the code in the `activities/demo-python` directory.
Feel free to fiddle with any of the code snippets.
Add your own, try things out and experiment!

In order to run a Python script, just type the name of the script preceded by `python3`:

```console
root@kali:~/essentials/welcome-to-linux/activities/demo-python# python3 variables.py
```

### Variables

Let's start with [variables.py](./activities/demo-python/variables.py).
This file explains how variables such as integers, floats and strings work in Python.
It also introduces the `print` function.
Inspect and run the code.
Note that, unlike C code, in Python there is no need for a `;` at the end of each line.

### If Statements

Now that we know how to create and print variables, let's learn some more of the language's syntax, starting with the `if` keyword.
A typical `if` statement looks like this:

```python
if condition:
    # run some code
```

Notice that there are no `{}`, like you would use in C.
This is because Python relies on **indentation** to determine which instructions make up the body of the `if` statement and which don't.
Moreover, a colon (`:`) needs to be used after every `if`, `for` or function declaration, as we'll see shortly.
To make things clearer, check out and run the code in `activities/demo-python/if.py`.

As stated above, this code would not work because the `print` instruction is not correctly indented and the `if` statement appears to have no body:

```python
if a == 0:
    print('This is an incorrect if statement. You will get an IndentationError.')
```

But don't take our word for granted.
Run this code too!

### Loops

Loops, be they `for` or `while` loops, use the same syntax as `if` statements:

```python
for var in set_of_objects:
    # for body

while condition:
    # while body
```

Once again, note the usage of the `:` after each loop declaration and the indentation of their bodies.

The `in` keyword present in the `for` loop above signifies that the `var` variable will act as an **iterator**.
At every step of the loop, `var` will be assigned to each consecutive element of  the collection `set_of_objects`.

As before, take a look at, run and play with the code in `activities/01-demo-python/loops.py` until you feel you get the hang of `for`s and `while`s.

### Functions

You've already seen the `print`, `range` and `reversed` functions.
It is natural that we now try to create our own functions.
They follow the same syntax as before:

```python
# As expected, the types of the parameters need not be specified.
# But you can do it if you want/need to.
def func(param1, param2):
    # function body
```

We can also specify a **default** value that a parameter can take when none is specified:

```python
def foo(param1, param2=5):  # param2 defaults to 5 when not specified
    # function body

# Both of these function calls are correct
foo('whatever')  # Here param2 = 5, by default
foo('whatever', 2)
```

By now, you already know what to do.
The demo for Python functions is in `activities/demo-python/functions.py`.
Go to town on it!

## Data Structures

Python comes equipped with built-in data structures, such as lists and dictionaries.

### Lists

Lists are indexed arrays that can store any type of data.
You can create a list by specifying its elements enclosed in `[]`:

```python
lst = [1, 'some string', True, 2.9]
```

Accessing the lists elements is similar to C: `lst[0]`, `lst[1]` and so on.
Yes, lists in Python are indexed from 0.

Now go ahead and get some practice with lists by using the `activities/demo-python/lists.py` script.

### Dictionaries

Conceptually, dictionaries are mappings between a set of **keys** and a set of **values**.
This means that **each key** is associated to **one value**.
The opposite does not always hold true.
Thus, each **key** in a dictionary is unique, but there is no such rule for **values**.

Let's construct a dictionary and see what it does:

```python
my_dict = {
    "SSS": "Rullz",
    "Essentials": 10,
    True: 0.2,
    2.2: 99
}

```

As you can see, neither the keys, nor the values in a dictionary need to be of the same type.

In order to access the value associated to a key, the syntax is the following:

```python
print(my_dict['SSS'])  # Will print "Rullz"
```

## Working with Files

Reading input from and writing output to is essential for any programmer.
We'll make heavy use of this feature in the future.

The main function for interacting with files is `open`.
Its simplified signature is the following:

```python
def open(filename, mode='rt'):
```

The `filename` parameter is self-evident.
The `mode` however, answers the question: "What do you want to do with this file?"
The `mode` parameter is a string, where each character has its own meaning.
The list of the most common characters is specified in [Python's official documentation](https://docs.python.org/3/library/functions.html#open).

Use <https://docs.python.org> whenever you need to look up some of Python's features.
For a quick intro into handling files in Python, consult the `activities/demo-python/files.py` script.
Run it, and then check the contents of the `output.txt` file it creates.

### Strings or Bytes?

In the previous section, we saw how we can read **strings** from and write them to files.
However, the more frequent way of interacting with files is by using **byte arrays**.

**Byte arrays** are very similar to strings, supporting nearly the same operations, but differ in representation.
While strings can also encode non-ASCII characters, such as `ä`, or even emoji, bytes are restricted to ASCII characters.
For this reason, one letter in a byte array is exactly one byte in size, whereas a letter in a string could use more space, depending on its encoding.
As a result, the main reason they exist is to process data, regardless of encoding.
Network packet data, binary file contents, images are all to be processed as bytes, not as strings.

You can create a byte array just like you would create a regular string **and adding a `b` in front**, like this:

```python
my_bytes = b'SSS Rulz, but in bytes!'
```

As always, the demo `activities/demo-python/strings_bytes.py` provides a more in-depth presentation of byte array and string operations.
Go take a look.

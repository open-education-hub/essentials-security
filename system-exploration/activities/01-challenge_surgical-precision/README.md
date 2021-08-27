# Surgical Precision

## Description

Your flags lie in files whose names are the either the answers to, or pointed at by the `question-*` files present in the `src` folder.

## Solution

### `question-1.txt`

There is but one true way of using Linux, and that is the **terminal**.

### `question-2.txt`

The `root` user is also known as the *privileged* user.

### `question-3.txt`

Look for hidden files in the `./flags` directory.

### `question-4.txt`

Remember:
- `find` looks at a file's metadata;
- `grep` looks at a file's data;
- `file` looks at a file's header.

### `question-5.bin`

As the name implies, this file is not a text file.
We said that the first step is to run the `file` command to see what file it is:
```
# file question-5.bin 
question-5.bin: data
```
There seems to be no special encoding.

Our next step is to use the `strings` command:
```
# strings question-5.bin 
OfUIA
os)a
Xp;|!$
h[A8
7.[a'
jmhr
b13=
1I*l
ViLm
Y"A5W
~]x=!P~
4]+-
You've already found the answer
4H5?,
2b\d
R_Z,
Vz|D
'g{A
	2i.
fJ.2
./Ya
:Y O
X|Jg
```

So the answer must be the command we've just used: `strings`.

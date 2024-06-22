# Continuing Our Exploration

In the challenge `Did You Look Everywhere` from the previous session, you had to **manually** look for the `.flag` file in the given hierarchy.
This, as you probably remember, was slow and frustrating.
We need some means by which to view **an entire hierarchy** at once, or to look for specific files.

Good news: such means do exist.

## Tree of Life

The `tree` command does what its name suggests: it displays a tree representation of a directory hierarchy.

```bash
root@kali:~# tree /lib/cryptsetup/
/lib/cryptsetup/
├── askpass
├── checks
│   ├── blkid
│   ├── ext2
│   ├── swap
│   ├── un_blkid
│   └── xfs
├── cryptdisks-functions
├── functions
└── scripts
    ├── decrypt_derived
    ├── decrypt_gnupg
    ├── decrypt_gnupg-sc
    ├── decrypt_keyctl
    ├── decrypt_opensc
    ├── decrypt_ssl
    └── passdev
```

We can also specify a **maximum depth** for `tree`'s traversal.
Look up the parameter in `tree`'s `man` page.
Once you've found it, use it in order to set a maximum depth of 2 for the `/opt` folder.
Your output should look like this:

```bash
root@kali:~# tree <add your paramtere here> /opt/
/opt/
├── google
│   └── chrome
└── Teeth
    ├── cache
    ├── etc
    ├── housekeep
    ├── README.txt
    ├── static
    └── units
```

Note that if you set the maximum depth to 1, `tree` essentially becomes a fancier looking `ls`.

## Find Your Way

As far as exploration goes, `tree` is a pretty strong tool.
It is capable of instantly displaying an entire file hierarchy.

But sometimes we have to deal with a large hierarchy in which we know what we're looking for.

As an example, let's look for the `memc.h` header file of the Linux kernel.
It's a small file that defines a tiny part of the communication between the GPU and RAM.
The header files corresponding to the version of your kernel are located in `/usr/src/linux-headers-5.6.0-kali2-common`.
Now go look for `memc.h`.
Good luck!
You should find it by... _tomorrow_.

But don't look for it manually.
This would be stupid.
You know what the name of the file is and you know the folder where to **find** it.
That's a lot of information already.
There is a Linux command that's useful for looking for files with certain particularities (such as names, size, access rights etc.) in a file hierarchy.
Which is exactly what we need!
This command is called `find`.
It outputs all files in a directory (and its subdirectories) that match some given properties.
Look up its syntax in the `man` page.
Look for the string "EXAMPLES".
It should lead you to a section at the end of the `man` page, which gives you a series of detailed examples of the command's usage.

From them and from the commands general description at the beginning of the `man` page, we can see that `find` is generally used like this:

```bash
root@kali:~# find <where to look> <what to look for>
```

- `<where to look>` is quite self-explanatory: it's a path in the file system, from where `find` will start to look for what we told it.
This means that `find` traverse the file system _down_ from the path it's given by looking exhaustively into each of its directories.
- `<what to look for>` is where things get more interesting.
We've already said that we can look for files that match certain properties, such as names, permissions, sizes, types and so on.
Each of these properties can be specified as follows:

`find` can take many more parameters, as described below.

## `type`

This parameter allows us to select either regular files (`-type f`), or directories (`-type d`) and so on.
Here's an example:

```bash
find /some/random/path -type d
```

This command will list all subdirectories in `/some/random/path`.

## `size`

Filters files by size.
For example, we can look for all files whose sizes are 100 bytes using this command

```bash
find /some/random/path -size 100c
```

The `c` at the end specifies that we're using bytes as unit of measurement.
The size can also be specified in:

- **kibibytes** (1024 bytes) using the letter `k`;
- **mebibytes** (1024 kibibytes) using the letter `M`;
- **gibibytes** (1024 mebibytes) using the letter `G`;

But looking for files with **exactly** a given size seldom happens.
It is more often the case that we're looking for files _smaller_ or _larger_ than some value.
For this reason, we may use the `-` (smaller) or `+` signs before the actual size, like this:

```bash
find /some/random/path -size +100k  # Find all files with a size larger than 100kB.
```

## `name`

This is the simplest property.
It's for when you're looking for a file with a certain name.
For finding the file `my_file`, it goes like this:

```bash
find /some/random/path -name my_file
```

This parameter is the one we need for our current task.
In order to find the file `memc.h`, we'll run:

```bash
root@kali:~# find /usr/src/linux-headers-5.6.0-kali2-common/ -name memc.h
/usr/src/linux-headers-5.6.0-kali2-common/arch/arm/include/asm/hardware/memc.h
root@kali:~# cat /usr/src/linux-headers-5.6.0-kali2-common/arch/arm/include/asm/hardware/memc.h
/* SPDX-License-Identifier: GPL-2.0-only */
[...]
#endif
```

## Globbing

But what if we only knew a portion of our filename?
Or what if we intentionally wanted to find all files ending in `.log`, for instance?

For this, we need to use the concept of **globbing**.
This mechanism defines a set of special characters that are interpreted differently than regular ASCII text.

## `*`: 0 or more characters

The `*` character is interpreted as any number of characters of any type.
Basically, `*` stands for everything and nothing.
Take a look at the example below:

```bash
root@kali:~# ls D*
Desktop:

Documents:

Downloads:
```

The `*` makes `ls`'s parameter **match** any filename that starts with `D`.
You can use `*` anywhere in your parameter.
Moreover, any command that takes a filename as input accepts the globbing syntax.
Here's another example:

```bash
root@kali:~# find /usr/src/linux-headers-5.6.0-kali2-common -name *group*  # List all linux kernel header files whose names contain the word "group"
/usr/src/linux-headers-5.6.0-kali2-common/arch/s390/include/asm/ccwgroup.h
[...]
/usr/src/linux-headers-5.6.0-kali2-common/include/uapi/linux/cgroupstats.h
```

The most commonly used globbing examples (apart from `*`) are listed below.

## `+`: one or more characters

This symbol is very similar to `*`.
However, `+` needs at least one character in order to match the specific string.

## Ranges

`[]` represents a _range_.
Let's look at the following range: `[a-f]`.
It starts at `a` and ends with `f`, inclusively.
`[0-9]`, for example, matches any digit.
Likewise, `[A-Z]` matches any capital letter, and so on.

You can combine ranges.
For instance, `[a-zA-Z]` matches any letter.

## Sets

In order to represent a set of characters to be matched, `{}` are used.
`{a,0,m,b}` matches _either_ `a`, `0`, `m` or `b`.

## Escaping

What if we want to match the `*` character itself?
Or any of the special characters above, such as `+`, `[`, `]`, `{` and `}`?
Obviously, we can match **any** character.
The special characters can be matched by **escaping** them.

Escaping is the practice of specifying that a symbol be interpreted as a regular character and not as part of a globbing expression.
This feature is achieved by placing a `\` character before any special globbing character that you want to escape.
Here are a few examples:

- `\*`: matches a literal `*`;
- `\[`: matches a literal `[`;
- `{\+,\}}`: matches either a literal `+`, or a literal `}`.

You can **combine** escaped characters and globbing expressions as you please.

## Redirecting Streams

Any process (remember that Linux commands are processes, too) uses 3 implicit data streams.

## Standard Input (`stdin`)

This is the "place" from where the process reads its data.
Many processes read data from the keyboard:

- `man`'s `stdin` is the keyboard because it reads user commands and interprets them in order to navigate the current `man` page.
- `bash`'s `stdin` is also the keyboard.
`bash` reads user input, that is typed into the terminal and then executes those commands.

The main alternative to getting input from the terminal is using a file.
Strictly from a teaching standpoint, unless given a file, `cat` reads its input from the terminal (kinda useless, we know).
Let's showcase the usage of `stdin` redirection.
First, let's use `cat` without redirection.

```bash
root@kali:~# cat  # Read input from the terminal.
SSS Rulz!
SSS Rulz!
^C
root@kali:~# # We used Ctrl + C to close the above cat process.
```

Now let's redirect `cat`'s input to a file.
We use `<` in order to redirect `stdin`.

```bash
root@kali:~# cat < essentials/README.md 
# Security Summer School: Security Essentials Track
[...]
```

Let's look more closely at what happens here, as opposed to running `cat essentials/README.md`:

- `cat essentials/README.md` makes the `cat` command itself open the `essentials/README.md` file and read bytes from it;
- `cat < essentials/README.md` has **the underlying `bash` process** read the `essentials/README.md` file and **feed its content** to `cat`, which is now reading input **from the underlying `bash` process**.

The same output is printed, but the mechanism now differs entirely.

### Standard Output (`stdout`)

`stdout` is the complement of `stdin`.
A processes output is generally displayed to `stdout`.
Generally, this stream is also the terminal.
We've already seen this feature when running almost any command so far.

```bash
root@kali:~# ls
Desktop    essentials           Music     Public         Videos
Documents  ghidra_9.1.2_PUBLIC  peda      %SystemDrive%
Downloads  libc-database        Pictures  Templates
```

We've seen this output may times in the previous session.
The names of the directories and files inside the current folder are printed **to `stdout`**, i.e. to the terminal.

Let's redirect `ls`'s output to a file:

```bash
root@kali:~# ls > ls_output
```

Notice that now there is _seemingly_ no output.
In reality, it does exist, but is written by `ls` to the `ls_output` file instead of the standard `stdout` stream (the terminal).

```bash
root@kali:~# cat ls_output  # The same files as before. Their layout changes, though.
Desktop
Documents
Downloads
essentials
ghidra_9.1.2_PUBLIC
libc-database
Music
out
peda
Pictures
Public
%SystemDrive%
Templates
Videos
```

## Standard Error (`stderr`)

Sometimes commands fail.
If you haven't encountered one, you haven't been using Linux for long enough.
Here's a simple error:

```bash
root@kali:~# ls whatever
ls: cannot access 'whatever': No such file or directory
```

The error message (`ls: cannot access 'whatever': No such file or directory`) is displayed to the terminal, so it would make sense for it to be printed by `ls` to `stdout`, right?
Well... no.
It's printed to another stream, called `stderr`.
As its name implies, this stream is dedicated to error messages.
This distinction was made in order for users to be able to separate between useful / legitimate output and sometimes unimportant error messages.

Redirecting `stderr` is performed using 2 characters: `2>`.

```bash
root@kali:~# ls whatever 2> ls_error
root@kali:~# # No error message. The error itself still did happen.
root@kali:~# cat ls_error  # I told you so...
ls: cannot access 'whatever': No such file or directory
```

## Appending

Let's redirect `ls`'s output multiple times:

```bash
root@kali:~# ls essentials > out
root@kali:~# cat out
application-lifetime
assembly-language
binary-analysis
data-representation
data-security
explaining-the-internet
hacking-the-web
README.md
rediscovering-the-browser
system-exploration
taming-the-stack
welcome-to-linux
root@kali:~# ls > out
root@kali:~# cat out
Desktop
Documents
Downloads
essentials
ghidra_9.1.2_PUBLIC
libc-database
Music
out
peda
Pictures
Public
%SystemDrive%
Templates
Videos
```

As you can see, when the second `ls` output is written to the `out` file, the first output is **overwritten**.
This sucks in case we want to generate large output files, such as logs.

But fear not!
Instead, remember last session's Python crash course.
More specifically, remember `open`'s parameters.
The second one was `mode` and one of the modes is _append_, symbolised by the `a` character.
This mode makes any text that's written to that specific file to be added at the end of whatever data was already inside it, without overwriting anything.

We need something similar to that, which can be achieved by using `>>` for redirecting `stdin` and `2>>` for redirecting `stderr`.
Here's how it works for the previous `ls` commands:

```bash
root@kali:~# ls essentials > out  # This command also creates the out file. It is irrelevant whether we use > or >>.
root@kali:~# cat out
application-lifetime
assembly-language
binary-analysis
data-representation
data-security
explaining-the-internet
hacking-the-web
README.md
rediscovering-the-browser
system-exploration
taming-the-stack
welcome-to-linux
root@kali:~# ls >> out  # This is where the overwriting took place. We've now changed command to use >>.
root@kali:~# cat out
application-lifetime
[...]
Videos
```

Lovely!

## Pipes

Up to now, we've looked at how to redirect the basic streams of a process to files.
But what if we wanted to redirect **one stream of a process into the stream of another process**?
Of course we can do this, too, by using the **pipe** (`|`).

To demonstrate the usage of pipes, we'll introduces the `tac` command.
Notice it's `cat` in reverse.
This is not arbitrary.
If `cat` displays the **lines** in a file **in order**, `tac` does the same, but **in reverse order**.
Let's exemplify using the global `README.md`:

```bash
root@kali:~# tac essentials/README.md
1. [Taming the Stack](./taming-the-stack)
1. [Assembly Language](./assembly-language)
1. [Binary Analysis](./binary-analysis)
1. [Application Lifetime](./application-lifetime)
1. [Data Security](./data-security)
1. [Data Representation](./data-representation)
1. [Hacking the Web](./hacking-the-web)
1. [(Re)Discovering the Browser](./rediscovering-the-browser)
1. [Explaining the Internet](./explaining-the-internet)
1. [System Exploration](./system-exploration)
1. [Welcome to Linux](./welcome-to-linux)
Sessions are:

There, you will find a `README.md` file with the session documentation and, if it's the case, subfolders with support data for the challenges.
Each session is located in its specific folder.

Welcome to the Security Essentials Track of the Security Summer School.

# Security Summer School: Security Essentials Track
```

Now let's actually use a pipe.
We'll also use a command from before, so we keep things simple.
Let's find all Linux kernel header files whose names contain the word "group" and then print them **in reverse order**:

```bash
find /usr/src/linux-headers-5.6.0-kali2-common -name *group* | tac
```

Notice this output is the one you saw in section [`*`: 0 or more characters](#-0-or-more-characters), but in reverse.

## `xargs`

We've seen how powerful pipes are.
Remember that pipes redirect the `stdout` of the first command into the second's `stdin`.
But what if we wanted to redirect the same `stdout` as command-line parameters for the second command?

This is when we would use `| xargs`.
Let's assume this hypothetical command:

```bash
cmd1 | xargs cmd2
```

where `cmd1` and `cmd2` are hypothetical commands.
The `| xargs` keyword makes **every line** from the `stdout` of `cmd1` be passed **as a separate parameter** to `cmd2`.

A very powerful use case of `xargs` is `find ... | xargs grep ...`.
Such commands allow us to look for strings in all files that match certain criteria **at once**.
Let's showcase this by inspecting all log files about the `systemd` process:

```bash
# find /var/log -type f -name *log | xargs grep systemd
```

## Less is More

Try running the following command:

```bash
root@kali:~# tree -L 2 /
```

You can see that its output is rather huge.
For large directory hierarchies, `tree`'s output can be overwhelming.
The same thing can happen when running `find` commands.

We've already seen how we can trim such outputs down by `grep`, but sometimes we have no criterion on which to do so.
In these situations, we have no alternative but to look at the entire output.
In order to do so in more easily, we can use the `less` command.

First of all, `less` can be used just like you would use `cat`.
Run the commands below.
You can navigate inside `less` the same way you can navigate inside `man`.
**And you definitely remember how to navigate inside `man`!**

```bash
root@kali:~# cat /var/log/syslog  # Never ending logs...
[...]
root@kali:~# less /var/log/syslog  # Much better.
```

Inside `less`, try searching for the string "network".

**Remember:** Don't scroll your terminal.
It doesn't look cool.
Use `less`!

## Grep

`find` has taught us how to use various criteria in order to filter through a file hierarchy.
This is definitely useful, but we can do better.
`find` is highly capable of filtering output based on the files' **metadata**, i.e. "surface level" information, such as sizes, names and so on.

It would be really useful if we had a means to filter files **based on their content**.
And we do!
This tool is called `grep`.
`grep` is capable of matching strings based on the contents of files, not just on their names.

Let's look for the `stdin` string in this README:

```bash
root@kali:~# grep "stdin" essentials/system-exploration/README.md
#### Standard Input (`stdin`)
- `man`'s `stdin` is the keyboard because it reads user commands and interprets them in order to navigate the current `man` page.
- `bash`'s `stdin` is also the keyboard.
Let's showcase the usage of `stdin` redirection.
We use `<` in order to redirect `stdin`.
`stdout` is the complement of `stdin`.
We need something similar to that, which can be achieved by using `>>` for redirecting `stdin` and `2>>` for redirecting `stderr`.
```

As you can see, `grep` outputs the **lines that contain the given string**.
This makes `grep` extremely useful for looking for CTF flags.
We simply need to `grep "SSS"`.

## Grep a File Hierarchy

At this point, you may be tempted to believe that we can only `grep` a single file.
Nope.
We can even `grep` strings in entire file hierarchies, which is extremely powerful.

Let's `grep` the `task_struct` symbol in our kernel's header files.
This symbol is a C `struct` that contains all the information associated with any Linux process.

```bash
root@kali:~# grep -R "task_struct" /usr/src/linux-headers-5.6.0-kali2-common | less  # The output is rather large, so we contain it with less.
```

**Remember this distinction:** `find` looks for file **metadata** (names, permissions, size, type), while `grep` looks for file **data**.

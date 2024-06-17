# Working with Linux

## I Command Thee

The most important shortcut when using a Linux operating system is `Ctrl + Alt + t`.
Try it now!
The dark box that has appeared is called a **terminal**.
A terminal is a means by which we can tell the operating system what to do for us.
In other words, we use the terminal in order to give **commands** to the operating system using a text interface, without the use of a mouse or fancy graphics.
Hence the terminal's alternative name: the **Command-Line Interface (CLI)**.
What you've been using until now, namely navigating the desktop environment by clicking on shortcuts, files and links is called the **Graphical User Interface (GUI)**.

Here are a few useful key shortcuts for navigating the terminal more easily:

- open another terminal window: `Shift + Alt + t`;

- navigate between open terminal windows: `Alt + N`, where `N` is the index of the tab you want to switch to **(starting from 1)**;

- close the current window: `Ctrl + d`;

- copy text from the terminal: `Ctrl + Shift + c`;

- paste text to the terminal: `Ctrl + Shift + v`.

It's kind of like a web browser, if you think about it, but with different key combinations.
Don't worry about memorising them now, though.
You'll get plenty of time to practice them in today's activities and in the sessions to come.
For more terminal shortcuts, see the section [More Terminal Tricks](./further-reading.md) below.

### The Prompt

Note that the line begins with `root@kali:~#`.
This is what is called a **prompt**.
It's like a sign that the current terminal is waiting for commands to execute.

The format of the prompt is the following:

```console
user@host_name: current_working_directory #
```

Now let's look at each of these components one by one.

- `user` is the name of the current user.
In our case, it says `root`.
We'll see what this means in its dedicated [section](#the-root-user) below.
We chan check that the user truly is `root` using the command `whoami`:

```console
root@kali:~# whoami
root
```

- `host_name` is the name of the current system.
Once again, we can check if `kali` truly is our hostname by running the command `hostname`

```console
root@kali:~# hostname
kali
```

- `#` is a sign that tells us that the prompt is over and that you can start typing commands.
It can also be `$` or `>`.

- `current_working_directory` is the **path** in the file system where we are currently located.
If this sounds confusing, don't worry.
We'll explain the file hierarchy right now.

### The File System

One of the most important things when we're using the CLI and after hacking a remote system is to know where we are in its file hierarchy.
This hierarchy is more commonly known as the **file system**.
The path separator in Linux is `/`, unlike Windows, where it's `\`.
At the same time, `/` is the root of the file system.

The file hierarchy looks like this:

![Sample File Hierarchy](../media/sample_file_hierarchy.svg)

Going back to the `current_working_directory` in the prompt, the terminal can also be seen as a file walker.
This means that at each moment it is "placed" in a certain directory, i.e. at some point in the file hierarchy.
We can see that the prompt shows `~`.
This stands for **the home directory of the current user**.
Our current user is `root` and its home directory is `/root`.
Let's check this by running the command `pwd` (print working directory):

```console
root@kali:~# pwd
/root
```

### Traversing the File System

Great!
So now we know **where** we are in the file system.
Let's see what's here in `/root`.
For this, we use `ls`, that simply lists the contents of the current directory:

```console
root@kali:~# ls
Desktop    ghidra_9.1.2_PUBLIC  peda      %SystemDrive%
Documents  libc-database        Pictures  Templates
Downloads  Music                Public    Videos
```

That's quite a bit of stuff, but there's no need to look into each of these now.
Let's focus on navigating the file system for now.

Almost every linux command, such as `ls`, can take various parameters that alter its behaviour.
`ls` for instance can list any given directory, not just the current directory.
This requires the use of the path to list as a parameter:

```console
root@kali:~# ls /  # list the contents of the / (root) directory
0     dev   initrd.img      lib32   lost+found  proc  sbin  tmp  vmlinuz
bin   etc   initrd.img.old  lib64   media       root  srv   usr  vmlinuz.old
boot  home  lib             libx32  opt         run   sys   var
root@kali:~# ls /media  # list the contents of the /media directory
cdrom  cdrom0
```

Notice the second `#` symbol in each command.
This one is different from the one in the prompt.
It marks the beginning of a comment, just like `//` does in C.

So we can now see what a given directory contains, but we're still stuck in `/root`.
Let's change our current directory. For this, we use `cd`:

```console
root@kali:~# ls libc-database/  # list the contents of libc-database
add  common  db  dump  find  get  identify  README.md  tmp

root@kali:~# cd libc-database/  # move to libc-database

root@kali:~/libc-database# ls  # list the contetns of the current directory (now libc-database)
add  common  db  dump  find  get  identify  README.md  tmp

root@kali:~/libc-database# pwd  # check that we really are in libc-database
/root/libc-database
```

Notice the prompt change to `~/libc-database` after `cd` because the current directory changes.

Stop!
**`Tab` Time!**
Almost every CLI is capable of autocompletion and that of Linux is no different.
Type `cd l` and then press `Tab`.
Notice that the rest of the directory's name has been autofilled: `cd libc-database/`.
Now type `cd D` and press `Tab` **twice**.
Notice that 3 options have appeared.
What happened is that the terminal found 3 directories that start with `D` and is asking you for more information.
Type `e` and press `Tab` once more.
Now the terminal sees there is only one option, `Desktop/` and autofills it for you.

`Tab` allows you to use the terminal very efficiently.
It's one of the most powerful tools at our disposal, so remember to abuse it as much as possible.
**Keep in mind: there is no such thing as pressing `Tab` too many times**.

Now back to our directories.
So we're in `libc-database`, but how do we get back to `/root`?
Similarly to a browser, the parent of any directory can be accessed using `..` like so:

```console
root@kali:~/libc-database# ls ..
Desktop    ghidra_9.1.2_PUBLIC  peda      %SystemDrive%
Documents  libc-database        Pictures  Templates
Downloads  Music                Public    Videos

root@kali:~/libc-database# cd ..

root@kali:~# ls
Desktop    ghidra_9.1.2_PUBLIC  peda      %SystemDrive%
Documents  libc-database        Pictures  Templates
Downloads  Music                Public    Videos

root@kali:~# pwd
/root
```

Makes sense?
Alright.
So now we can move anywhere.
We can chain paths using the separator (`/`), even adding `..`, like so:

```console
root@kali:~/libc-database# cd ../..  # we are in /root/libc-database

root@kali:/# ls  # now we are 2 levels up, in /
0     dev   initrd.img      lib32   lost+found  proc  sbin  tmp  vmlinuz
bin   etc   initrd.img.old  lib64   media       root  srv   usr  vmlinuz.old
boot  home  lib             libx32  opt         run   sys   var
```

### Be a Man

Almost every Linux command comes with extensive documentation.
This documentation can be read using `man <command>`.
Let's try reading the manual page for the `ls` command:

```console
root@kali:~# man ls
```

- Use `↑` and `↓` to scroll up and down.

- Use `Space` to scroll one whole page down.

- Use `/<string>` to search for any string.
Try searching for the string "recursive".
Use `n` to navigate to the next occurrence of your string and `Shfit + n` to navigate to the previous one.

- Use `q` to quit the manual

**Task 1:** Use the parameter you've just found to recursively list the contents of the `/root/libc-database` directory, using both relative and absolute paths.

**Task 2:** Use the man page for `ls` again to learn how to view the contents of a directory in the form of a **long listing**.
This parameter will show you more details regarding a file, such as its type, size, owner, access rights, the date when it was last modified etc.
Test it on the file `/root/libc-database/README.md`

**Task 3:** Use the man page for `ls` to find out what parameter to pass to `ls` to list **all** entries in a directory.
This option will also show you the **hidden** files in that directory.
These files start with `.`.
Test it on the `~` directory.
Notice our friend `..` is also present.

### I'll Make My Own Hierarchy

In order to create directories we use the `mkdir` command:

```console
root@kali:~# mkdir demo

root@kali:~# ls
demo     Documents  ghidra_9.1.2_PUBLIC  Music  Pictures  %SystemDrive%  Videos
Desktop  Downloads  libc-database        peda   Public    Templates

root@kali:~# cd demo

root@kali:~/demo# 
```

Now let's create a file in our new directory.
For this, we use the `touch` command.
It creates an **empty** file.

```console
root@kali:~/demo# touch demo-file

root@kali:~/demo# ls
demo-file

root@kali:~/demo# cat demo-file  # The file is empty, so nothing is printed.

root@kali:~/demo# touch demo-file2  # Just because we can.

root@kali:~/demo# ls
demo-file  demo-file2
```

In order to remove a file, we use the `rm` command.

```console
root@kali:~/demo# rm demo-file2

root@kali:~/demo# ls
demo-file
```

Now let's try to remove our directory the same way.

```console
root@kali:~# rm demo
rm: cannot remove 'demo': Is a directory
```

Deleting a directory requires that an extra parameter be passed to `rm`.
Find it in `rm`'s `man` page.
Look for the string "recursively".
Yup, it's `-r` (or `-R`, or `--recursive`; all three work).

```console
root@kali:~# rm -r demo/

root@kali:~# ls
Desktop    ghidra_9.1.2_PUBLIC  peda      %SystemDrive%
Documents  libc-database        Pictures  Templates
Downloads  Music                Public    Videos
```

All clean!

### Absolute or Relative?

There are two ways of expressing a file path: relative and absolute.
**Relative** paths are called so because they refer to the current directory.

```console
root@kali:~# cd libc-database/
```

This command  uses a **relative** path, as `libc-database` only exists in `/root` (`~`).
If we were to run it from `/bin` for instance, it wouldn't work because there is no `libc-datbase` directory in `/bin`.

**Absolute** paths however can be used from anywhere in the filesystem.
They contain the full path to the file, starting from the root of the file system (`/`):

```console
root@kali:/lib/x86_64-linux-gnu/security# cd /root/libc-database/
root@kali:~/libc-database# pwd
/root/libc-database
```

In the snippet above, we were able to navigate to `/root/libc-database` from somewhere completely different in the hierarchy.

Let's get some practice:

- Navigate to `/usr/lib/dpkg/methods/apt/`, but don't just copy and paste this path.
Use `Tab` and you'll barely have to type anything.

- Now get back to `root`'s home using the home directory shortcut.

- Navigate to `~/ghidra_9.1.2_PUBLIC/docs/images` using its absolute path.

- Now move 2 levels up the hierarchy without retyping the path.
Use `..`.

### Inspecting File Contents

Up to this point, we've learned how to traverse the file system.
Now we need to be able to *inspect* the files themselves.
The simplest ways to view the contents of a file in the terminal is the `cat` command:

```console
root@kali:~# cat /etc/hostname 
kali
```

As you've probably guessed, `/etc/hostname` is the file where the machine's hostname is stored.

Feel free to consult `cat`'s man page for further details about the command.
We'll introduce more advanced means of outputting the contents of a file in the session dedicated to [Data Representation](../data-representation).
Stay tuned!

## The Root User

As we said previously, the prompt may indicate the current user, in our case `root`.
But what exactly is this user?
Well, Linux systems admit multiple levels of user privileges.
These privileges refer to the actions a certain user is allowed to perform, such as installing other apps or reading various files.

But among all users, there is *one to rule them all*: `root`.
Similar to the `Administrator` user in Windows, `root` has no restrictions to the actions he may perform.
This is the default user in Kali Linux, so you don't need to worry about permissions.
However, when logging into the remote servers we provide for some of the CTF challenges below, the user will be `ctf` and it **does** have limited permissions.

## Processes

Now that we've learned how to use the terminal, let's take a look at the desktop.
A few common apps are pinned to the left taskbar.
Any application that is installed on a system is called a **program**.
One such program is the web browser **Firefox**
By clicking the Firefox icon, the **program** starts to run.
Any running program is called a **process**.

Let's test this by learning a new command.
With Firefox closed, run the command `ps`.
Use `man` to learn what it does.
If you use it as-is in the terminal, it displays two running processes: `bash` and `ps` itself:

```console
root@kali:~# ps
    PID TTY          TIME CMD
   1929 pts/0    00:00:00 bash
   3304 pts/0    00:00:00 ps
```

- `bash` stands for *Bourne-Again Shell* and is the command interpreter used by the terminal.
In other words, it's what reads your input and executes the commands you type.

- You already know what `ps` is.
But why is it here?
You see, in order for `ps` to start scanning for what processes are running, it needs to be running itself, which means it's inevitable that it finds itself while scanning.

Now open Firefox from the side bar and run `ps` again:

```console
root@kali:~# ps
    PID TTY          TIME CMD
   1929 pts/0    00:00:00 bash
   3304 pts/0    00:00:00 ps
```

Where is Firefox?
Well, when run without parameters, `ps` displays the processes that are running **inside the current terminal**, i.e. that have been started from this terminal.
Firefox was started from the GUI, so it has nothing to do with our terminal.
Use `man` to learn how to list the **full** output of **all** processes in the system.

Hopefully you haven't cheated and did find the `-A` (or `-e`) and `-f` options yourself.
Now the output is rather huge, but we only care about the final lines:

```console
root@kali:~# ps -A -f
[...]
root        3367    1612 50 15:54 ?        00:00:01 /usr/lib/firefox-esr/firefox-esr
root        3444    3367 20 15:54 ?        00:00:00 /usr/lib/firefox-esr/firefox-esr -contentproc -childID 1 -isForBrowser -prefsLen 1 -prefMapSize 183434 -parentBuildID 20200527211442 -greomni /usr/lib/firefox-esr/omni.ja -appomni /usr/l
root        3498    3367 14 15:54 ?        00:00:00 /usr/lib/firefox-esr/firefox-esr -contentproc -childID 2 -isForBrowser -prefsLen 5670 -prefMapSize 183434 -parentBuildID 20200527211442 -greomni /usr/lib/firefox-esr/omni.ja -appomni /us
root        3549    3367 35 15:54 ?        00:00:00 /usr/lib/firefox-esr/firefox-esr -contentproc -childID 3 -isForBrowser -prefsLen 6402 -prefMapSize 183434 -parentBuildID 20200527211442 -greomni /usr/lib/firefox-esr/omni.ja -appomni /us
root        3590    3367 10 15:54 ?        00:00:00 /usr/lib/firefox-esr/firefox-esr -contentproc -childID 4 -isForBrowser -prefsLen 6402 -prefMapSize 183434 -parentBuildID 20200527211442 -greomni /usr/lib/firefox-esr/omni.ja -appomni /us
root        3623    1929  0 15:54 pts/0    00:00:00 ps -A -f
```

Great success!
We have seen Firefox move from being a simple program to being a running process.
In addition, we've learned a new command that is useful for inspecting what processes might be running on a system.
Once you hack into a remote system, you can use `ps` to inspect what potentially exploitable processes are there.

## Scripts

It is often convenient to group together a set of instructions so that you don't have to type them separately each time you want to make use of their combined functionality.
For this purpose, you can use Bash scripts.
They are text files that simply contain Bash commands.
Bash is also a programming language that comes with `if` statements, `for` loops, functions and more, but we won't be needing those right now.

Bash scripts typically bear the extension `.sh`, but this is by no means mandatory.
Take some time to take a look at and run the Bash script in `activities/demo-bash/demo.sh`.
You can run it like so:

```console
root@kali:~/essentials/welcome-to-linux/activities/demo-bash# sh demo.sh
```

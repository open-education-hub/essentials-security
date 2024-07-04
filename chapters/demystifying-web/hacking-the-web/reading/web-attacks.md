# Web Attacks

## Path Traversal

Every request asks for a file.
Remember `GET /path/to/file`.
Even `GET /` implicitly asks for `index.html` or `index.php`.

If the application does not verify the parameter, an attacker might be able to exploit the application and display an arbitrary file from the target system.
Normally an attacker would try to access sensitive files containing passwords or configurations in order to gain access to the system.
Remember that PHP scripts aren't normally visible by the client.

Below is an example of a vulnerability where an attacker can leak PHP scripts:
Consider the following URL:

```plaintext
http://somesite.com/view.php?file=image.jpg
```

What if the attacker could query the website using `view.php` as parameter?

```plaintext
http://somesite.com/view.php?file=view.php
```

This would be too easy.
Sometimes, images are stored in different directories than application files.
So our attacker should query the server like with a link like this one:

```plaintext
http://somesite.com/view.php?file=../../view.php
```

If they manage to view `view.php`, then it is likely they can access any file on the system, such as `/etc/passwd`, using this query:

```plaintext
http://somesite.com/view.php?file=/etc/passwd
```

This kind of situation when an attacker can freely access files on the server is called a **path traversal attack**.
To fix this, applications should always validate user input and ensure the path they request is within a safe folder to which they have access.

## DIRectory Buster (DIRB)

There may be other files stored on the server that aren't accessible from the entry point web page.
It is difficult to search for such pages manually.
Luckily there are tools that can help us with this.
One of them is **DIRectory Buster**, or `dirb` in short.
It simply queries a web server for many files **fast**.
All you need to do is to give it a list of files for which to search.

Here's how to run it:

```console
root@kali:~# dirb <URL> wordlist.txt
```

A good starting point for wordlists are the lists [here](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content), particularly those named `raft-large-*.txt`:

- `raft-large-files.txt` for files, duh...
- `raft-large-directories.txt` for directories

`dirb` works by issuing lots of `GET` requests, one for each file in its wordlist.
If a request receives a 404 response, the file doesn't exist.
Otherwise, it does (except for 500 responses, in which case the request is resent).
Even a 403 response is alright.
It just means that a regular user doesn't have access to that file.

Here's what `dirb` + [`SecLists`](https://github.com/danielmiessler/SecLists) look like:

```console
root@kali:~# dirb http://example.com ~/SecLists/Discovery/Web-Content/raft-large-files.txt
[...]
---- Scanning URL: http://example.com/ ----
+ http://example.com/index.html (CODE:200|SIZE:1256)
+ http://example.com/. (CODE:200|SIZE:1256)
+ http://example.com/extension.inc (CODE:403|SIZE:345)
[...]
```

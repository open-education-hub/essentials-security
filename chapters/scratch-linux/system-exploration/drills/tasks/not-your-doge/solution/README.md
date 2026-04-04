# Not Your Doge: Solution

The header of the image is this:
```
P6
500 500
255
```
According to this header, the image should have `500 * 500 * 3 = 750000` bytes of data.

However, the file size is 1032016 bytes:
```
root@kali:~# ls -l essentials/activities/05-challenge_not-your-doge/src/not-doge.pnm
-rw-r--r-- 1 root root 1032016 Aug 26 22:03 not-doge.pnm
```

The difference between the actual file size and that of the displayed image is: `1032016 - 750000 = 282016`.
This is way too much for that small header we've just seen.
The meme is probably _cut_, but the missing bytes are still inside the file.
Only the header was tampered with.
More precisely, some of the bottom bytes are not displayed.

Since the header's format is plaintext, we can change it in any text editor, or use Python.
Increasing the height manually to **688** pixels reveals the full image.

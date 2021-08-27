# Not Your Doge

## Description

You are given an image, that contains a well-known meme.
The meme is incomplete.
Go ahead and find the missing part.

## Solution

`.pnm` images use RGB colours expressed in binary format.
This means, that every 3 bytes make up one colour.
Apart from those bytes, there is a small header consisting of the minimum amount of information required to correctly display the image:
- encoding: `P6`;
- width and height: `500 590`;
- maximum byte value: `255`.

The header is essentially this:
```
P6
500 590
255
```

Let's inspect the file's size:
```
root@kali:~# ls -l essentials/activities/05-challenge_not-your-doge/src/not-doge.pnm
-rw-r--r-- 1 root root 1032016 Aug 26 22:03 not-doge.pnm
```

It's 1032016 bytes. Now let's see what its header says:
```
root@kali:~# file essentials/activities/05-challenge_not-your-doge/not-doge.pnm 
not-doge.pnm: Netpbm image data, size = 500 x 590, rawbits, pixmap
```

Let's do some maths: `500 * 590 * 3 = 885000` bytes.
So the difference between the file's actual size and that of the displayed image is: `1032016 - 885000 = 147016`.
This is way too much for that small header we've just seen.
There must be some hidden information.

The meme looks cut, so the hidden info hypothesis might hold.
More precisely, it is likely that some of the bottom bytes are not displayed.
Since the header's format is plaintext, we can change it in any text editor, or use Python.

Increasing the height manually to **688** pixels reveals the full image.

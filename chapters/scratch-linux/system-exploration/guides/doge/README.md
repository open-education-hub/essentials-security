# Doge

The best way to showcase the `strings` command is to use it in order to find our first flag for today.
Head to the `guides/doge/support` folder and take a look at the image you've been given.

Since this section is dedicated to the `strings` command, we'll run this command on our `doge.jpg` file:

```bash
root@kali:~/essentials-security/chapters/scratch-linux/system-exploration/guides/doge/public# strings doge.jpg
JFIF
[...]
eP!_"
```

So there are lots of human-readable strings in this image, but very few, if any, actually make any sense.
In order to filter them out, we'll use what we've learned today: `|` + `grep`.
We'll try to find the flag itself.
Maybe we get lucky.

```bash
root@kali:~/essentials/system-exploration/activities/doge/public# strings doge.jpg | grep SSS
<there should be a flag here>
```

That's how you use `strings`: often in combination with some filtering mechanism, such as `grep`.

Another way to get the flag is to run the `file` command:

```bash
root@kali:~/essentials/system-exploration# file activities/doge/public/doge.jpg
activities/doge/public/doge.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "SSS{grep_your_strings}", progressive, precision 8, 500x500, components 3
```

The flag is included in the file as a comment.
Image comments are often used in CTFs in order to hide some more subtle information, such as hints.
Always remember to check them out.

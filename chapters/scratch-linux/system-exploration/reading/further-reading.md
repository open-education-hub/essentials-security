# Further Reading

## Forensics

The greater CTF topic of today has been **forensics**.
It's probably one of the vastest and most diverse topics out there, because it doesn't really fit into many patterns.
You can read more about forensics [here](https://trailofbits.github.io/ctf/forensics/).

### Regular Expressions

Regular expressions are like globs on steroids.
They provide a huge step-up in terms of expressiveness.
As expected, they're also more difficult to understand.

By default, `grep` actually matches regular expressions, not just raw strings.
`find` can also look fore files matching regular expressions, by using the `-regex` and `-regextype` parameters (yes, there are multiple regular expression syntaxes).

A good point from which to start learning how to use regular expressions are these resources:

- `https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285`
- `https://regexone.com/`

For testing your regular expressions before using them, [this website](https://regex101.com/) is king.

Once you've got the hang of regular expressions, test your skills in the [regular expression Crossword](https://regexcrossword.com/).
Yes, such a thing really does exist and it's as crazy as you might think.
Give it a try!

Moreover, most programming languages have libraries for regular expressions.
Python can do so, too.
Take a look at its [regular expression module](https://docs.python.org/3/library/re.html).

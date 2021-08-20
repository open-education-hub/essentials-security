# Jumbled

## Description

You get a flag that is made up of jumbled chunks from the real flag, split by `\x80\x80\x80` bytes.
You have to recreate the original flag.

### Solution

There are no hints by which you can figure out the original flag.
As a result, you need to create all possible flags and try them out one by one.
That is, take the chunks present in the `flag` file and generate all their permutations until you find the real flag.

**The moral of the story:** Sometimes the brute force method is the way to go.

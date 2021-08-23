# Did You Look Everywhere?

## Description

You are given access to a seemingly uninteresting system.
`ls` shows that a file hierarchy is present in the `/home/ctf` directory.
Upon inspecting it, all files _seem_ to be empty.

## Solution

Running `ls -a` inside `/home/ctf/south-park/al-gore/manbearpig` reveals a hidden file called `.flag`.
Inspecting its contents with `cat .flag` displays the flag.

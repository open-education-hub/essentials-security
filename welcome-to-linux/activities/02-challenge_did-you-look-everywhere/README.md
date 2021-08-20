# Did You Look Everywhere?

## Description

You are given access to a seemingly uninteresting system.
`ls` shows nothing in the `/home/ctf` directory.

## Solution

Running `ls -a` reveals a hidden file called `.flag`.
Inspecting its contents with `cat .flag` reveals the flag.

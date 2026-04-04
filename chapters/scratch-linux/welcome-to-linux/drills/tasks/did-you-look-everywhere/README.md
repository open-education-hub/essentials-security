# Name: Essentials: Welcome to Linux: Did You Look Everywhere?

## Description

You are given access to a seemingly uninteresting system.
`ls` shows that a file hierarchy is present in the `/home/ctf` directory.
Upon inspecting it, all files _seem_ to be empty.

Score: 100

## Exploit

Running `ls -a` inside `/home/ctf/south-park/al-gore/manbearpig` reveals a hidden file called `.flag`.
Inspecting its contents with `cat .flag` displays the flag.

Use the commands in `./sol/solution.sh`.

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

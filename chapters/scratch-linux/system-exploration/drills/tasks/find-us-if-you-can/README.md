# Name: Essentials: System Exploration: Find Us If You Can

## Description

This challenge has you look for two flags.
Once found, the first flag gives you a hint about how to find the second flag.

Score: 200

## Exploit

Run the script in `./sol/solution.sh`.

## Environment

Linux container that students can log onto using `ssh`.

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

# Name: Essentials: System Exploration: Empty Files

## Description

The `/home/ctf/south-park` folder houses a large hierarchy of files.
Most of them are empty.

Score: 100

## Vulnerability

Some of the files contain letters.
The concatenation of these files, sorted lexicographically, is the flag.

## Environment

Linux container that students can log onto using `ssh`.

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

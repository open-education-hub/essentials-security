# Name: Essentials: Explaining the Internet: Unaccessible

## Description

Connect to `141.85.224.70` with user `vuln`, on port `3222` and get the flag.
Whoops, you don't know the password.
You have its MD5 hash in `password.txt`.

Score: 100

## Exploit

Use [`john`](https://github.com/openwall/john) to find out the password.

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

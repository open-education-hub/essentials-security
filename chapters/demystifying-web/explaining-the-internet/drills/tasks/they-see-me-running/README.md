# Name: Essentials: Explaining the Internet: They See Me Running

## Description

There is a quiz server on this system.
Upon each correct answer, it grants you a flag.

Score: 100

## Exploit

Use `netstat -tlpn` to find the port on which the server is listening.
Then answer its questions.

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

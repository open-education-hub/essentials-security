# Name: Essentials: Explaining the Internet: Pinger

## Description

The server uses `ping` to check if another host is online.
Just give it the IP of the host you want to check... and something more.

Score: 100

## Vulnerability

The `ping` server calls `subprocess.Popen('ping -c 1 ' + user_input)`.
This leaves it vulnerable to a command injection attack.

## Exploit

Script in `./sol/solution.sh`

## Environment

Web server with Flask (deployable as a Docker container using files in `deploy/` folder)

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

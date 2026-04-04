# Name: Name

## Description

Do what the server tells you.

Score: 100

## Vulnerability

The flag is displayed only if access http://141.85.224.118:8089/name/the_flag.html.

## Exploit

Script in `./sol/solution.sh`


## Environment

Apache web server. (deployable as a Docker container using files in `deploy/` folder)

## Deploy

Deployment is done via Docker using the `Dockerfile` and support files in the `deploy/` folder.

Copy the challenge folder to the remote hosting system, enter the `deploy/` folder and run `make run`.
This will create and deploy the Docker container with the proper port redirection in place.

If you need to update the image and container, first use `make clean` to remove the old container, then use `make` to update the image (and the container).
It is not possible to update the container without updating the image first.

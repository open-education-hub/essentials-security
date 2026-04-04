# Name: Readme

## Description

Do what the server tells you.

Score: 25

## Vulnerability

The flag is showing up in the URL after clicking on the hyperlink.

## Exploit

Script in `./sol/solution.sh`

## Environment

Apache web server. (deployable as a Docker container using files in `deploy/` folder)

## Deploy

Copy `deploy/` folder and run `make run`.

If you need to update the image and container, remove the old container with `make clean` and update the image (and container) using `make`.

It is not possible to update the container without updating the image first.

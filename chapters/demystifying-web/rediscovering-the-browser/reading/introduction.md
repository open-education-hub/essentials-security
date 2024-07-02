# (Re)Discovering the Browser

## Introduction

In this session we'll zoom in on one of the application-level protocols mentioned in session [Explaining the Internet](../explaining-the-internet/): HTTP.
We'll explain how the browser works and what information to draw from the most widely spoken language on the internet: HTML.
In addition, we'll also imitate the behaviour of our browser using two highly-versatile commands: `curl` and `wget`.

## Reminders and Prerequisites

For this session, you'll need:

- a high-level understanding of the TCP/IP stack explained in session [Explaining the Internet](../explaining-the-internet/)
- an internet connection
- a Firefox/Chrome browser
- a Linux command-line interface

## Web Applications

A typical web application is essentially a server.
A server is a host connected to the internet that **listens** for connections from **clients**.
A client is any application that interacts with the server.
So in short, the server waits for clients to come to it.
The clients are proactive.
They reach out to the server by initiating connections.

![Web Application Model](../media/client-server.svg)

## Web Security

There are 3 main subjects when it comes to web security:

- client-side security (i.e. browser security)
- server-side security
- communications security (i.e. the security of the data while it's travelling from client to server or vice-versa)

In this track, we'll discuss about server-side security as attacking servers is by far the most rewarding out of the 3 options above.
Since servers communicate with lots of clients, infecting one server can allow an attacker to steal data or even infect the server's clients as well.

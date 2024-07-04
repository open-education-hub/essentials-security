# Introduction

[Last session](../../rediscovering-the-browser/) we learned how browsers work, what HTTP and HTML are and how to use `curl` and `wget` to imitate a browser.
Today we'll dive deeper into the inner workings of browsers.
Specifically, we will:

- learn how to use the developer tools to inspect the requests it makes
- learn what cookies are
- learn how to use them from the command-line
- learn how to write Python scripts that send HTTP requests

## Reminders and Prerequisites

Remember these concepts from the [previous session](../../rediscovering-the-browser/):

- by default, HTTP is a **stateless** protocol.
Every request is independent from any other
- HTTP supports fixed methods, such as `GET`, `PUT`, `POST` etc.
- HTTP servers respond with status codes and, optionally, data.
- web browsers such as Firefox are HTTP clients
- `curl` and `wget` are used to send HTTP requests and to download files, respectively

For this session, you need:

- a working internet connection
- basic knowledge of the HTTP protocol
- a Linux machine
- a Firefox browser
- a Python interpreter (at least Python3.6)

## Sending HTTP Requests from Python

The module we need in order to handle requests in Python is called `requests`.
It contains methods for all types of HTTP requests: `GET`, `POST`, etc.

```python
import requests as req

URL = 'https://httpbin.org'

# Send a `GET` request.
# `params` is a dictionary of query parameters.
# `response` is an object.
response = req.get(f'{URL}/get', params={'name': 'SSS', 'role': 'boss'})
# This request is equivalent to:
# GET URL?name=SSS?role=boss

# We must access its fields to gain specific information.
print(response.status_code)  # The status code returned by the server
print(response.text)  # The HTML sent by the server

payload = {'skill': 'infinite'}
response = req.post(f'{URL}/post', data=payload)
```

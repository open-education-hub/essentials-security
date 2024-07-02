# Summary

HTTP is the most widely used protocol for passing data on the internet.
It is a stateless protocol, meaning that each request is independent from any other request, even for the same resource.
It allows a few specific methods:
    - `GET` - request data from the server
    - `POST` - upload data to the  server
    - `PUT` - update data on the server
    - `DELETE` - remove data from the server

Each request is like a function call across the web and can receive parameters.
In a URL, they are separated from the path by `?` and from each other by `&`.
They are key-value pairs such as `?user=hacker&role=god`.

The two commands we've added to our arsenal today are `curl` and `wget`:

- `curl`: create and send HTTP requests.

Here are some of its most useful parameters:
    - `-v`: **verbose** - display the request and response headers.
    - `-d`: **data** - specify the body of a request (usually a `POST` request) and the query parameters
        - `-G`: **get** - allows sending a body in a `GET` request
    - `-X <method>`: use another HTTP method than the default `GET`
    - `-L`: **follow redirects** - issue another request to the redirected URL the when receiving a `3XX` response.

- `wget`: download files

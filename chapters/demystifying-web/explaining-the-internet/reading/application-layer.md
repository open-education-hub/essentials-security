# The Application Layer

The layer that is the closest to the user, the application layer is also the one that is hardest to define, since it denotes all network applications.
So we'll try to list but a few examples of applications.
We've already mentioned some of them in the [TCP](./transport-layer.md#tcp) and [UDP](./transport-layer.md#udp) sections.

In essence, every app that you use, and which has anything to do with the internet, is implemented at the application layer.

## `netstat`

Netstat is a complex service used for inspecting various networking-related data.
We'll be using it to list the services running on a host.
Now let's test our own Kali Linux host.

List all running services.
The `-a` parameter stands for "all".

```console
root@kali:~# netstat -a | less
```

That's quite a lot of them.
Let's trim them down a bit.
For example, let's only list the services running TCP connections.
The `-t` parameter stands for "TCP".
Notice how we can concatenate parameters.
`-a -t` is equivalent to `-at` or `-ta`.

```console
root@kali:~# netstat -at | less
```

Similarly, we can query all services using UDP connections:
As you might have guessed, UDP connections are listed using the `-u` parameter.

```console
root@kali:~# netstat -au  # no need for `less` anymore
```

Now let's look for **servers** specifically.
Usually a server waits for clients to connect to it and send requests.
We say the server **listens** for connections.

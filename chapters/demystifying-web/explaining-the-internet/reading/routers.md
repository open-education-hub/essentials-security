# Routers

It is impossible to connect your PC / laptop directly (physically) to every PC or server in the world.
Therefore, we need **networks**, which are basically aggregations of hosts (servers, PCs, laptops, mobile phones etc.).

Each network contains one **router** which sends data between the hosts in its network and those on other networks.
So a router is a networking device that connects two or more networks.
Think of the router you most probably have at home.
There is a *local network*, to which you can connect via Wi-Fi, or Ethernet cables.
You're probably doing this right now.
Another network is the one provided by your Internet Service Provider (ISP).

There are many ISPs around the world and even more local home networks.
The web thus becomes a *web of routers* who transmit **packets** from one network to another.
Back to our example above, you will surely need many routers to get a packet from the US to India.

But how does a router know how where to send a packet?
Let's say a router R1 connects a laptop with IP `192.168.100.5` and a PC with IP `192.168.100.10` to the external network, as shown in the image below.

![Router in Action](../media/router_in_action.svg)

Now let's look at 2 different scenarios:

1. If the laptop sends a packet to IP `192.168.100.10`, the router knows this address is part of its **Local Area Network (LAN)** and sends it directly to the PC.
1. If the PC sends a packet to `upb.ro` (with IP `141.85.220.33`), the router sees its IP as an external address.
Therefore, it passes it into the internet, where other routers take it and then pass it again to other routers and so on, until the packet reaches `upb.ro`.

Each new router that a packet encounters on its way from source to destination is called a **hop**.
Most often, a hop is a router.
In order to visualise the hops that our requests to a well-known service, such as `google.com`, we use the `traceroute` command:

```bash
┌──(kali㉿kali)-[~]
└─$ traceroute google.com
traceroute to google.com (142.250.185.206), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.212 ms  0.123 ms  0.228 ms
 2  10.20.21.254 (10.20.21.254)  2.815 ms  3.908 ms  3.838 ms
 3  109.101.201.49 (109.101.201.49)  4.894 ms  4.971 ms  4.810 ms
 4  193.231.103.0 (193.231.103.0)  9.634 ms  9.467 ms  9.359 ms
 5  10.0.241.109 (10.0.241.109)  8.547 ms  9.129 ms  9.958 ms
 6  * * *
 7  10.0.240.194 (10.0.240.194)  59.356 ms  39.555 ms 10.0.200.6 (10.0.200.6)  39.579 ms
 8  10.0.240.121 (10.0.240.121)  39.426 ms  39.373 ms  38.338 ms
 9  92.87.30.10 (92.87.30.10)  42.521 ms  39.938 ms  41.795 ms
10  * 10.252.185.126 (10.252.185.126)  40.778 ms *
11  142.250.226.148 (142.250.226.148)  38.924 ms 172.253.73.152 (172.253.73.152)  41.083 ms 108.170.252.1 (108.170.252.1)  42.216 ms
12  142.250.225.77 (142.250.225.77)  39.563 ms 108.170.252.18 (108.170.252.18)  40.317 ms 142.250.225.77 (142.250.225.77)  36.148 ms
13  fra16s52-in-f14.1e100.net (142.250.185.206)  40.195 ms 209.85.242.79 (209.85.242.79)  39.355 ms 108.170.236.249 (108.170.236.249)  38.919 ms
```

Let's explain the output.
Each line represents a **hop** (i.e. a router) that a packet must pass through in order to reach `google.com`.
The first number is the index of the hop.
The second is the *IP* of the network.
You've probably heard about IPs before.
We'll demystify them in a bit.
`traceroute` sends 3 packets, for consistency.
It counts the time it takes from sending each of these packets to the moment the response reaches the sender.
This time is called **Round Trip Time (RTT)**.
As we said, `traceroute` sends and monitors 3 packets in order to display the consistency of the link to each hop.

The first hop is between the VM and the host.
The other is the router to which the host is connected.
From then on, it's the wild internet itself.

## IP Addresses

IP addresses or, in short, **IPs**, are 32-bit (i.e. 4 bytes) numbers used to identify **hosts**.
IP stands for **Internet Protocol**, which is the most widely used internet layer protocol.
Notice the difference between IPs and MACs.
While MACs are associated with NICs, IPs are associated with hosts.
Another difference is that whereas a MAC is unique to and engraved into the NIC, a host can change its IP more easily.
We won't go into this in today's session, but you can read about one such mechanism called [DHCP](./further-reading.md#dhcp).

Of course you are free to express an IP address however you like, but by far the most common representation is to write each of its 4 bytes individually, in the decimal base, separated by a dot (`.`).
You've already seen IPs when connecting to the remote hosts during the previous sessions.
Some IPs are:

- `8.8.8.8`: is the address of Google's Public DNS Service.
We'll explain what the DNS is in a future [section](./further-reading.md#dns).
- `69.63.176.13`: is a common IP address used by Facebook
- `141.85.224.100`: is IP the address of one of the machines in our CTF infrastructure

In order to see the IP of your machine, run the following command:

```bash
┌──(kali㉿kali)-[~]
└─$ ip address show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:3c:2a:8d brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 86379sec preferred_lft 86379sec
    inet6 fe80::262a:29ff:8129:db77/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

Your output may differ slightly.

An IP address is associated with a **network interface**.
These interfaces can be virtual or physical (present on your NIC).
In your Kali VM, all interfaces are virtual.

**`lo`** is the **loopback** interface.
It's an internal interface that each host possesses.
Its purpose is for testing the OS's TCP/IP stack.
Its IP is, by convention `127.0.0.1`, or `0.0.0.0`.

**`eth0`** is the interface used to connect to the internet.
It acts as a middleman between your host OS (the one in which you're running the VM) and the guest OS (Kali).
Its status is *UP* (i.e. it's running) and its IP address is `10.0.2.15`.

Notice the `/24` part.

### `ping`

In order to test whether a host is up or down, we can `ping` its IP.
`ping` sends packets to the given host (IP or website) and reports whether the host responds or not.
If it responds, it's obviously alive.
Otherwise... it's complicated.
It can either be dead itself, **or there can be no route to it**.
If we consider that the connection between us and our pinged host is *mediated* by a chain of routers, as shown in the image above, if **one** of those routers is down and doesn't transmit packets, then we may be unable to reach the pinged host.
So a better wording is to say that when a host doesn't respond to pings, it's not necessarily *down*, but merely **unreachable**.
From a host's point of view though, it's irrelevant whether a host is down for real or not.
An unreachable host is as good as a dead one: *useless*.

`localhost`, in other words the `lo` interface, should **always** be up and respond to pings.
In case it doesn't, well... your kernel's TCP/IP stack may be broken.
We use the `-c 3` parameter to only send 3 "pings" to `localhost`.
Otherwise, `ping` sends packets continuously, until stopped manually (with `ctrl + c`).

```bash
┌──(kali㉿kali)-[~]
└─$ ping -c 3 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.040 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.060 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.046 ms

--- 127.0.0.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2053ms
rtt min/avg/max/mdev = 0.040/0.048/0.060/0.008 ms
```

`ping` also tells us the RTT to the pinged host.
Notice the very small times when pinging ourselves.
This makes sense, since there are no hops (routers) between a host and itself.

Now let's `ping` a remote server, say `google.com`.
We can `ping` either an IP or a URL.

```bash
┌──(kali㉿kali)-[~]
└─$ ping -c 3 google.com
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=39.0 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=50.1 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=44.6 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 39.031/44.556/50.078/4.509 ms
```

Now the RTTs are longer, because of the routing taking place between our VM and `google.com`.
The more routers on the way, the longer the RTT.

# Further Reading

## The OSI Stack

In the session, we discussed the TCP/IP stack, which is implemented by the kernel of every Operating System (Linux included).
In the early days of the internet, however, another model was popular.
This was the **OSI Model**.
As a matter of fact, it's still a popular model for teaching about the internet, because it makes a more rigorous separation of what we called the Application Layer.
This layer is split into 3, and the transmission medium is added as a separate physical layer, thus resulting a 7-layer stack.
You can learn about this alternative stack [here](https://www.imperva.com/learn/application-security/osi-model/), but keep in mind that it is almost never used in practice.

## The Networking Bible

Speaking of the OSI model, it is paramount that we mention the most influential book in computer networking to this day, namely Andrew Tanenbaum's [Computer Networks](http://index-of.es/Varios-2/Computer%20Networks%205th%20Edition.pdf).
Dating from 1981 (about the time these stacks were first defined), this book has been the cornerstone of networking ever since.
It's a must-read for every networking enthusiast.

## ICMP

The protocol used by `ping` is called **Internet Control Message Protocol (ICMP)**.
The protocol defines a set of _utility_ messages and responses, used by hosts in order to check the status of other hosts.

There is also a very well-known attack, called **Distributed Denial of Service (DDoS)**, by which an attacker floods a server with `ping`s essentially.
The purpose of this attack is to overwhelm the server by making it do nothing else but respond to these `pings`, rather than serve the actual requests for which it was designed.
Thus, this type of attack aims to render a server useless, or even make it crash.
The attack has been executed in many forms, with one of the simplest being described [here](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/).

## URL vs URI

This session you've learned about _URL_'s, but you might have also heard about _URI_'s.
They're quite similar, but still different.
[Here](https://danielmiessler.com/study/difference-between-uri-url/)'s the difference explained.

## IPv6

Since regular IPs (also known as **IPv4**) are 32-bit numbers, there are `2^32` possible unique IPs.
This number may look large, but it's _just_ 4,294,967,296, so just upwards of 4 billion.
But the world's population is 7.9 billion as of September 2021, and growing.
The pigeonhole principle tells us there are not enough IPs so that every human can be connected to the internet at the same time.

For this reason and some others related to the lack of native security of the IP protocol, a new iteration of IPs was designed: **IPv6**.
These new IPs are 128-bit numbers.
`2^128` is 39 **digits** long, so it should suffice for the entirety of Earth's population (a few times over).

For a better (but still short) introduction to IPv6, check out [this](http://www.steves-internet-guide.com/ipv6-guide/) source.

## DHCP

**Dynamic Host Configuration Protocol (DHCP)** is a protocol used in order to manage and distribute IP addresses.
Hosts are _leased_ IP addresses from DHCP servers for a limited amount of time.
When an address is about to expire, a host can ask the server to extend the lease.
You can read more about DHCP servers [here](https://www.infoblox.com/glossary/dhcp-server/).

## Containers

The main difference between containers and VMs is that VMs use their own separate OS, whereas containers share the OS with the host.
Think about your Kali Linux VM.
It obviously has a separate OS: Kali Linux, duh, while you have your own OS: Windows, Linux, macOS, whatever.
The operating system inside the VM is called **guest OS**, while the "outer" OS is called **host OS**.
When it comes to VMs, you need some sort of _mediator_ between the guest and the host.
This mediator is called **a hypervisor**.
In your case, this is VirtualBox.

This separation between OSs ensures a more secure separation between the two environments.
On the other hand, if a host spawns multiple containers, all of them (host and containers) use the host's OS.
The containers are most importantly separated at the filesystem level.
They can also be allocated more limited resources.
Notice that if you were to use a container for the Security Summer School, you couldn't use Kali Linux unless your host OS were also Kali Linux, which would have been pretty pointless.

![Containers vs VMs](../media/containers-vs-virtual-machines.png)

However, we use containers to host challenges because our VMs and containers all use Linux and because we can house more containers on the same host (which is itself a VM) than we could VMs.
You can learn more about containers and how to manage them using `docker` (we also use it for challenges) [here](https://www.docker.com/resources/what-container/).

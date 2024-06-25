# Summary

We've used a lot of acronyms during this session.
Here they are explained once more, in case you missed some of them:

- **ACK:** Acknowledgment
- **(D)DoS:** (Distributed) Denial of Service
- **DHCP:** Dynamic Host Configuration Protocol
- **DNS:** Domain Name System
- **HTML:** HyperText Markup Language
- **HTTP(S):** HyperText Transfer Protocol (Secured)
- **ICMP:** Internet Control Message Protocol
- **IMAP:** Internet Access Message Protocol
- **IP:** Internet Protocol
- **ISP:** Internet Service Provider
- **LAN:** Local Area Network
- **MAC:** Media Access Control
- **NACK:** Not Acknowledged
- **NIC:** Network Interface Card
- **OSI:** Open Systems Interconnection
- **POP3:** Post Office Protocol version 3
- **RTT:** Round-Trip Time
- **SMTP:** Simple Mail Transfer Protocol
- **SSH:** Secure Shell
- **TCP:** Transmission Control Protocol
- **TLD:** Top-Level Domain
- **UDP:** User Datagram Protocol
- **URI:** Uniform Resource Identifier
- **URL:** Uniform Resource Locator

Here's a short summary of the layers of the TCP/IP stack:

- **Link:** Provides us with direct connections to other hosts.
Also adds identifiers to NICs in the form of MAC addresses.
- **Internet:** Provides routing and identifiers for hosts in the internet, in the form of IP addresses.
- **Transport:** Provides connections between processes on different hosts by using ports.
- **Application:** Composes the actual message to be delivered to the receiver.

Finally, let's map some of the layers of the TCP/IP stack to the command-line tools we use for each of them:

- **Internet:**
  - `ping`
  - `dig`
- **Transport:**
  - `ssh`
  - `netcat`
- **Application:**
  - `netstat` (although it has [many other uses](https://linux.die.net/man/8/netstat))

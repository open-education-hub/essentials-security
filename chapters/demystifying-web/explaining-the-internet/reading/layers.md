# Layers on Layers on Layers

As we said previously, each of the layers of the TCP/IP model adds its own information to the data coming from the layer above.
This encapsulation at each layer results in a new structure effectively wrapping up the original data.
Each of these has a specific name depending on the layer that creates it:

| TCP/IP Layer | Name of data block produced by the layer |
|:------------:|:----------------------------------------:|
| Application  | Application data (e.g. HTTP, HTTPS)      |
| Transport    | Segments (TCP) or datagrams (UDP)        |
| Internet     | Packets (e.g IP packet)                  |
| Link         | Frames (e.g. Ethernet frame)             |

## The Medium

This layer is not mentioned in the above diagrams, but is worth talking a little bit about.
The medium represents the connection itself between the 2 stations.
This connection can be:

- **wired**: using a cable on which digital signals that encode the bits are sent
- **wireless**: using high-frequency radio waves in order to send the same signals as before

## The Link Layer

This layer is also known as the **Data Link** layer.

It represents the underlying technology of any application.
The device on which the application is running may have a choice of many technologies to connect to a network, such as Ethernet, Wi-Fi, Bluetooth, 4G, 5G (_tinfoil hat off_) etc.
Where more than one link exists, the operating system of the device chooses the most appropriate link.
For instance, a mobile phone might be connected to both 4G and Wi-Fi.
Most mobile phones prefer the Wi-Fi connection, but remain connected to 4G mobile data, which they use as backup.
However, in some cases the application itself may dictate the choice of link, e.g. the mobile phone may decide to send traffic over Wi-Fi to avoid 4G data charges.
Once the link has been chosen, the appropriate link layer protocol is selected.

The most commonly used link layer protocol is **Ethernet**.
Wired or wireless Ethernet is used on most local area networks (LANs).
The packets from the internet layer are further encapsulated in Ethernet frames which are designed to be transported across a local network.

This layer needs a means to identify local stations.
This is where the **Media Access Control (MAC) addresses** come in.
They are 48 bits long and are unique to a specific **Network Interface Card (NIC)**.
The MAC address is physically tied to the hardware of the computer, which means it may also be referred to as the hardware or physical address.

## The Internet Layer

So each NIC has its own 48-bit MAC address.
This means there are `2^48` unique MACs, which means `2^48` unique NICs.
`2^48` is a huge number, which is way beyond everything humanity has produced so far.
So, since we aren't likely to run out of MAC addresses any time soon, a host can be easily identified in the internet via its MAC, right?
Yes, it can.

There is one problem, though.
Suppose the sender is in the US and the receiver is in India.
There's no way you can connect these two hosts using the same medium.
You need some intermediaries: **routers**.

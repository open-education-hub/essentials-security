# A General Overview of the Internet

Before learning how to use and, later, how to hack the internet, let's first understand its building blocks.
The internet is all about sending data to and from an enormous amount of hosts.

In order to learn how all of this works, let's start from the example below.
It's generic enough for it to be relatable to most networking scenarios.
Yet, it encompasses everything we need to talk about.

![Network Stack](../media/network_stack.png)

So what happens here is that the computer on the left is trying to **send** data to the one on the right.
We call the left computer **the sender** and the right one **the receiver**.
The two computers are connected via a **medium** on which the actual bits of data that make up the communication are sent.
In short, this medium is the connection between the aforementioned computers.

However, there are 4 boxes above the aforementioned medium.
These boxes are altogether known as **The TCP/IP Network Stack**.
We'll see what's with the *TCP/IP* part soon enough.
Individually, each box is a **layer**.
Here are the 4 layers of the TCP/IP stack:

![The TCP/IP Network Stack](../media/tcp_ip_network_stack.svg)

Each layer provides a well-defined set of requirements, which are fulfilled by **protocols**.
A networking protocol is a set of rules that define the communication (data formatting and processing) between the same two levels of the network stack.
For example, there are protocols for the transport layer, others for the link layer and so on.
We'll talk about them in a bit.

## Encapsulation

Each layer takes care of a specific requirement of networking, as we'll discuss shortly.
When sending data, each of the layers in the TCP/IP model accepts data from the layer above (or from the user in the case of the application layer), and adds additional information to the data that is necessary for that layer to carry out its task.
In some cases, the original data may be processed in some way before the additional information is added.
For example, it might be encrypted.
The layer then passes this data on to the layer below (or onto the transmission medium in the case of the link layer).

The arrival of data from an upper layer may trigger additional separate messages to be sent to the receiving end.
For instance, if the data needed to be encrypted, the layer that carries out the encryption has to exchange initial setup messages with the receiving end to agree the encryption method and other data that we'll touch on in the session [Data Security](../data-security), before the encrypted data can be transferred.

At the receiving end, the process happens in reverse: each layer accepts data from the layer below, inspects and removes the additional information added on by the corresponding layer in the sending end, before passing it up to the layer above.

Data is passed from a sender process to a receiver process by using the services of the layer below.
It is only the final layer that actually causes the data to be transmitted onto the transmission media (e.g. cable).
Below is a representation of this whole mechanism.

![General Workings of a Network Stack Layer](../media/network_layers.png)

This method of modular communication is called **encapsulation**.
It can be likened to taking the data from the layer above and placing it in an **envelope**, writing some additional information on the envelope, then passing the envelope to the layer below.
At the receiving end, a layer is passed an envelope from the layer below.
It looks at the data on the outside of the envelope to decide what to do with the contents of the envelope.
It then opens the envelope and passes the contained data up to the next level.
The reverse of encapsulation is **decapsulation**.
After a message has passed through the network stack, it ends up in a *matryoshka* of envelopes, one for each layer, each with its own, specific information.

# Fundamental IT Networking Concepts

## 1. Network
A **network** is a collection of computers, servers, mainframes, network devices, peripherals, or other devices connected to one another to allow the sharing of data.

## 2. IP Address
An **IP Address (Internet Protocol Address)** is a unique string of numbers separated by periods that identifies each computer using the Internet Protocol to communicate over a network.

## 3. TCP/IP
**TCP/IP (Transmission Control Protocol/Internet Protocol)** is the suite of communications protocols used to connect hosts on the Internet. TCP/IP uses several protocols, the two main ones being TCP and IP.

## 4. DNS
**DNS (Domain Name System)** is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources.

## 5. Router
A **router** is a networking device that forwards data packets between computer networks. Routers perform the traffic directing functions on the Internet.

## 6. Switch
A **switch** is a device in a network that connects other devices together. Multiple data cables are plugged into a switch to enable communication between different networked devices.

## 7. Firewall
A **firewall** is a network security device that monitors incoming and outgoing network traffic and permits or blocks data packets based on a set of security rules.

## 8. VPN
**VPN (Virtual Private Network)** extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network.

## 9. LAN vs. WAN
- **LAN (Local Area Network)** is a network that connects computers and devices in a limited geographical area such as home, school, computer laboratory, or office building.
- **WAN (Wide Area Network)**, in contrast, spans a large geographic area such as a city, state, or country.

## 10. Network Protocol
A **network protocol** is a set of established rules that dictates how to format, transmit and receive data so computer network devices — from servers and routers to endpoints — can communicate regardless of the differences in their underlying infrastructures, designs or standards.

## 11. DHCP
**DHCP (Dynamic Host Configuration Protocol)** is a network management protocol used on IP networks whereby a DHCP server dynamically assigns an IP address and other network configuration parameters to each device on a network so they can communicate with other IP networks.

## 12. IPv4
**IPv4 (Internet Protocol version 4)** is the fourth version of the Internet Protocol (IP). It is one of the core protocols of standards-based internetworking methods in the Internet, and was the first version deployed for production in the ARPANET in 1983. It still routes most Internet traffic today, despite the ongoing deployment of IPv6.

## 13. IPv6
**IPv6 (Internet Protocol version 6)** is the most recent version of the Internet Protocol (IP), the communications protocol that provides an identification and location system for computers on networks and routes traffic across the Internet. IPv6 was developed to deal with the long-anticipated problem of IPv4 address exhaustion, and is intended to replace IPv4.

## 14. OSI Model
The **OSI Model (Open Systems Interconnection Model)** is a conceptual framework used to understand network interactions in seven layers:
  - **Layer 1: Physical** (cables, switches)
  - **Layer 2: Data Link** (Ethernet, switches)
  - **Layer 3: Network** (IP, routers)
  - **Layer 4: Transport** (TCP, UDP)
  - **Layer 5: Session** (establishes, manages and terminates connections)
  - **Layer 6: Presentation** (encryption, data conversion)
  - **Layer 7: Application** (HTTP, FTP, SMTP)

## 15. Communication Protocols and Examples
- **TCP (Transmission Control Protocol)**: Ensures reliable communication and data transfer.
- **UDP (User Datagram Protocol)**: Used for streaming media and online games due to lower latency.
- **ICMP (Internet Control Message Protocol)**: Used for diagnostic purposes, like ping.
- **Ethernet**: A family of protocols used in LANs, defines wiring and signaling for the physical layer.

## 16. Transmission Media
Transmission media can be classified into two types:
- **Wired** (Ethernet cables, fiber optics)
- **Wireless** (Wi-Fi, satellite)

## 17. Network Types: Client-Server and Peer-to-Peer
### Client-Server Networks
In a **Client-Server** network, computers and devices are assigned roles as either clients or servers. A **server** is a computer designed to process requests and deliver data to other (client) computers over a local network or the internet. Servers tend to have higher processing power, memory, and storage capabilities to manage the demands of multiple clients. This architecture is widely used in business environments, online services, and as the backbone of the internet.

- **Advantages**:
  - Centralized control and management of resources and data.
  - Easier to implement security policies and backups.
  - Scalability: It's relatively easy to add more servers or upgrade existing ones to accommodate more clients.

- **Disadvantages**:
  - Server dependency: If the server goes down, clients lose access to resources and services.
  - Cost: Servers can be expensive to purchase and maintain.

### Peer-to-Peer Networks
A **Peer-to-Peer (P2P)** network allows direct data exchange between participants (peers) without the need for a central server. In this setup, each peer acts as both a client and a server. This model is commonly used for sharing files (like in torrenting), blockchain networks, and certain messaging applications.

- **Advantages**:
  - No need for a central server, reducing cost and eliminating a single point of failure.
  - Direct file transfer between peers can be faster than downloading from a central server.
  - Scalable and resilient as adding more peers can increase the network's capacity and robustness.

- **Disadvantages**:
  - Less secure than client-server networks as it's harder to implement centralized security measures.
  - Data integrity and availability depend on the peers, which may come and go unpredictably.
  - Managing data consistency and preventing data redundancy can be challenging.

## 18. Routing Protocols Overview
Routing protocols are sets of rules or standards that dictate how routers communicate with each other, passing information that enables proper packet forwarding within a computer network. These protocols are categorized into two main types: Interior Gateway Protocols (IGP) and Exterior Gateway Protocols (EGP). Below are some of the most well-known routing protocols:
### Interior Gateway Protocols (IGP):

1. **RIP (Routing Information Protocol)** - One of the oldest routing protocols, utilizing the Bellman-Ford algorithm. It's simple to implement but has limited features.

2. **OSPF (Open Shortest Path First)** - An advanced interior routing protocol that uses link state information to compute the shortest path using Dijkstra's algorithm.
3. **IGRP (Interior Gateway Routing Protocol)** - Developed by Cisco, this routing protocol was designed for large networks and was replaced by EIGRP.
4. **EIGRP (Enhanced Interior Gateway Routing Protocol)** - An enhanced version of IGRP, also developed by Cisco. It's a hybrid protocol that combines the advantages of both distance vector and link state protocols.
5. **IS-IS (Intermediate System to Intermediate System)** - Similar to OSPF, it's a link state routing protocol used in some large networks, especially in ISP environments.
### Exterior Gateway Protocols (EGP):
1. **BGP (Border Gateway Protocol)** - The primary exterior gateway protocol (EGP) currently in use, facilitating routing information exchange between different Autonomous Systems (AS). BGP is a key element of the global Internet's functionality.

These protocols differ in their routing algorithms, efficiency, scalability, and application areas. Choosing the right protocol depends on several factors, including network size and topology, performance requirements, and available hardware.

## 19. IPv4 Addressing
IPv4 addresses are 32-bit numbers that uniquely identify a device on an IP network. They are usually written as four decimal numbers separated by dots (e.g., 192.168.1.1), with each part ranging from 0 to 255. Here's how IPv4 addresses are structured and used:
- **IP Address Structure**: An IPv4 address is divided into two parts: the network portion and the host portion. The division is determined by the subnet mask.
- **Subnetting**: Dividing a network into smaller sub-networks to improve efficiency and security. This involves adjusting the subnet mask to allocate more bits to the network portion.
- **Classes of IP Addresses**: Traditionally, IPv4 addresses were categorized into classes (A, B, C, D, E) based on the initial bits of the address and the network/host division. This system is less relevant today due to CIDR (Classless Inter-Domain Routing).
- **CIDR Notation**: An alternative to the traditional classful addressing, allowing for more flexible subnetting and efficient use of IP addresses (e.g., 192.168.1.0/24).
- **Private and Public IP Addresses**: IPv4 reserves certain address blocks for private use within networks (e.g., 192.168.x.x, 10.x.x.x, 172.16.x.x to 172.31.x.x). Public IP addresses are used on the internet and must be unique worldwide.
- **NAT (Network Address Translation)**: Allows multiple devices on a private network to share a single public IP address, facilitating internet access without assigning a unique public IP to each device.

## 20. MAC Addresses
A MAC (Media Access Control) address is a unique identifier assigned to network interfaces for communications on the physical network segment. MAC addresses are used as a network address for most IEEE 802 network technologies, including Ethernet and Wi-Fi. Here are key points about MAC addresses:
- **Format**: A MAC address is a 48-bit number, typically expressed as six pairs of hexadecimal numbers separated by colons (e.g., 01:23:45:67:89:ab).
- **Uniqueness**: MAC addresses are uniquely assigned to each network interface card (NIC) by the manufacturer, ensuring global uniqueness.
- **Function**: In a local area network (LAN), MAC addresses are used to physically locate and identify devices so data packets can be correctly routed to their destinations at the data link layer (Layer 2 of the OSI model).
- **ARP (Address Resolution Protocol)**: Used to map an IP address to its corresponding MAC address so that data packets can be correctly delivered in a network.

## Learning Resources
- **[Sieci komputerowe E13 E15 E16 EE08](https://www.youtube.com/playlist?list=PLOYHgt8dIdoz2fyn0gv4fs2t4tayalsh3)** - basic information about the network.
- **[Adresowanie IP v4. Budowa adresów, obliczenia, podział na podsieci](https://www.youtube.com/watch?v=t3IceGlTjig)** - the video about addressing IP addresses version 4.
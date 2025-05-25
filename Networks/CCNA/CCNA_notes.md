# Cisco Certified Network Associate (CCNA)

## Definitions

* `Protocol` in networking, is a set of logical rules defining how network devices and software should work.
* `Standard` in networking, is ????????
* `Internet Protocol` (IP)
    * is the Layer 3 address
    * `IPv4`
        * CLASS (prefix)            First Octet            Networks            Addresses per Network                                Details                                             Network Range
        
            Class A (8)               0xxxxxxx                128                   16,777,216                  0 - 126 (127.0.0.0/8 is preserved for the Loopback addresses)       0.0.0.0 - 127.255.255.255

            Class B (16)              10xxxxxx              16,384                    65,536                    128 - 191 (/16)                                                     128.0.0.0 - 191.255.255.255

            Class C (24)              110xxxxx             2,097,152               256 (254 hosts)              192 - 223 (/24)                                                     192.0.0.0 - 223.255.255.255

            Class D                   1110xxxx                                                                  224 - 239 (Multicast addresses)                                     224.0.0.0 - 239.255.255.255

            Class E                   1111xxxx                                                                  240 - 255 (Reserved / experimental addresses)                       240.0.0.0 - 255.255.255.255

        * Network address - all 0s(0)       i.e. 192.168.1.0
        * Broadcast address -all 1s(255)    i.e. 192.168.1.255
    * `IPv6`
* `Transmission Control Protocol` (TCP)
* `Address Resolution Protocol` (ARP)
    * it is used to discover the Layer 2 address (MAC address) of a known Layer 3 address (IP address).
    * `ARP Request` is sent to all hosts of the network (broadcast)
    * `ARP Reply` is sent to a specific host (unicast)
* `Internet Control Message Protocol` (ICMP)
    * it is used to test reachability by measuring round-trip time
    * `ICMP Echo Request`
    * `ICMP Echo Reply`

## Networking Models

Networking models categorize and provide a structure for networking protocols and standards.

#### 1. Open System Interconnection (OSI) Model

`OSI model` is a conceptual model that categorizes and standardizes the different functions in a network. It was created by the `International Organization for Standarization` (ISO) in the early 1980s

* L1 - Physical
    * defines physical characteristics of the medium used to tranfer data between devices (voltage levels, max transmission distance, physical connectors, cable specs, etc.)
    * digital bits are converted to electrical/radio signals

* L2 - Data Link ----> `L2 trailer | DATA | L4 header | L3 header | L2 header` = `FRAME`
    * provides node-to-node connectivity and data transfer
    * defines how data is formatted for transmission over a physical medium (i.e. copper UTP cables)
    * detects and possibly corrects Physical Layer errors
    * Switches operate in this layer

* L3 - Network ----> `DATA | L4 header | L3 header` = `PACKET`
    * provides connectivity between and hosts on different networks
    * provides logical addressing (IP addresses)
    * provides path selection between source and destination
    * Routers/PCs/Firewalls operate in this layer

* L4 - Transport ----> `DATA | L4 header` = `SEGMENT`
    * segments and reassembles data for communication between end hosts
    * breaks large pieces of data into smaller segments which can be more easily sent over the network and are less likely to cause transmission problems if errors occur.

* L5 - Session ----> `DATA`
    * controls sessions (dialogues) between communicating hosts
    * establishes / manages / terminates connections between local apps and remote apps

* L6 - Presentation
    * it translates data between 'application' format and 'network' format
    * encryption / decryption

* L7 - Application
    * closest to end-user
    * interacts with software applications
    * HTTP/HTTPS
    * identifying communication partners
    * synchronizing communication

#### 2. TCP/IP Suite

`TCP/IP Suite` is a conceptual model and set of communication protocols used in internet and other networks. It was developed by the US DoD through DARPA (Defense Advanced Research Projects Agency)

* L1 - Link ( = Physical + Data Link )
    * switch-to-switch data flow
* L2 - Internet ( = Network )
    * router-to-router data flow
* L3 - Transport
    * host-to-host data flow
* L4 - Application ( = Session + Presentation + Application )
    * process-to-process data flow

#### 3. Protocol Data Units (PDUs)
* Bit (L1 PDU)
* Frame (L2 PDU)
    * minimum size is 64 bytes
    * Preamble (7 bytes: 10101010 * 7)
    * Start Frame Delimiter (SFD) (1 byte: 10101011)
    * Frame = Preamble + SFD + Header + Payload (Packet) + Trailer
    * `Header` (14 bytes)
        * Destination (6 bytes) : Destination Media Access Control (MAC) address
            * Organizationally Unique Identifier (OUI) (3 bytes) is the first 3 bytes
            * Total 12 hexadecimal chars: xx.xx.xx.xx.xx.xx
        * Source (6 bytes) : Source Media Access Control (MAC) address
        * Type / Length (2 bytes) : If the value is <= 1500 indicates the `length` of the encapsulated packet in bytes. If it is >= 1535, then it indicates the `TYPE` of the encapsulated packet - usually IPv4 (0x0800 = 2048), IPv6 (0x86DD = 34525) or ARP (0x0806 = 2054), and the length is determined via other methods
    * `Trailer` (4 bytes)
        * Frame Check Sequence (FCS) (4 bytes) : Detects corrupted data by running a Cyclic Redundancy Check (CRC) algorithm over them.
* Packet (L3 PDU)
    * minimum size 46 bytes
    * Packet = Header(IPv4 or IPv6) + Segment
    * IPv4 `Header`
        * `Version` (4 bits) : IPv4 = 4 (0100), IPv6 = 6 (0110)
        * `IHL (Internet Header Length)` (4 bits) : Identifies the length of the header in 4-byte increments. Minimum = 5 (20 bytes), Maximum = 15 (60 bytes)
        * `DSCP (Differentiated Services Code Point)` (6 bits) : Used for QoS, prioritize delay-sensitive data
        * `ECN (Explicit Congestion Notification)` (2 bits) : Provides end-to-end notification of network congestion without dropping packets. It is optional
        * `Total Length` (16 bits) : Identifies length of the packet (L3 header + L4 segment) in bytes. Minimum = 20 bytes, Maximum = 65,535 bytes
        * `Identification` (16 bits) : Same value for all fragments of a packet. Packets are fragmented if larger than MTU (Maximum Transmission Unit) which is usually 1500 bytes which is the maximum size of an Ethernet frame.
        * `Flags` (3 bits) : Used to control/identify fragments
            * Bit #0: Reserved (always set to 0)
            * Bit #1: Don't Fragment (DF bit), used to indicate a packet that should not be fragmented
            * Bit #2: More Fragments (MF bit), set to 1 if there are more fragments in the packet, set to 0 for the last fragment
        * `Fragment Offset` (13 bits) : indicates the position of the fragment within the original, un-fragmented IP packet
        * `Time To Live` (8 bits) : Indicates a hop-count - each time the packet arrives at a router, the router decreases the TTL by 1. It is used to prevent infinite loops. A router will drop a packet with TTL of 0. Recommended default TTL is 64.
        * `Protocol` (8 bits) : Indicates the protocol of the encapsulated L4-PDU.
            * TCP = 6
            * UDO = 17
            * ICMP = 1
            * OSPF (Open Shortest Path First) = 89 (dynamic routing protocol)
        * `Header Checksum` (16 bits) : A calculated checksum used to check for errors in the IPv4 header. When a router receives a packet, calculates the checksum of the header and compares it to the one in this field of the header.
        * `Source IP Address` (32 bits)
        * `Destination IP Address` (32 bits)
        * `Options` if IHL > 5 (0, 320 bits) : Rarely used
* Segment (L4 PDU)
* Data (L5 PDU)

## Ethernet (Layer 1)
* is a collection of network protocols/standards.
* internet speed is measured in bites / second (bps)
* Ethernet Standards are defined in the IEEE 802.3 (1983)

#### 1. UTP copper cables
* RJ45
* Ethernet (10BASE-T)           / 802.3i    / 10 Mbps   / 100m / 2 pairs / straight-through or crossover
* Fast Ethernet (100BASE-T)     / 802.3u    / 100 Mbps  / 100m / 2 pairs / straight-through or crossover
* Gigabit Ethernet (1000BASE-T) / 802.3ab   / 1 Gbps    / 100m / 4 pairs / bidirectional
* 10 Gig Ethernet (10GBASE-T)   / 802.3an   / 10 Gbps   / 100m / 4 pairs / bidirectional    

* straight-through cables (full-duplex):1+2 -> 1+2, 3+6 -> 3+6
* cross-over cables (full-duplex):1+2 -> 3+6, 3+6 -> 1+2

#### 2. Fiber-optic cables
* Fiber-optic (1000BASE-LX) / 802.3z    / 1Gbps     / 5 km (single-mode) or 550 m (multi-mode) 
* Fiber-optic (10GBASE-SR)  / 802.3ae   / 10Gbps    / 400 m (multi-mode)
* Fiber-optic (10GBASE-LR)  / 802.3ae   / 10Gbps    / 10 km (single-mode)
* Fiber-optic (10GBASE-ER)  / 802.3ae   / 10Gbps    / 30 km (single-mode)

NOTE_1: IEEE = Institute of Electrical and Electronics Engineers.

NOTE_2: (BASE-T) BASE = Baseband signaling, T = twisted pair

NOTE_3: UTP = Unshielded Twisted Pair


## Switches (Layer 2)
* have many network interfaces/ports for end hosts to connect to.
* provide connectivity to hosts within the same Local Area Network (LAN).
* Tx: 3+6.
* Rx: 1+2.
* Auto-MDIX / RJ45 for UTP cables.
* Small Form-Factor Pluggable (SFP) Tranceiver for fiber-optic cables.
* MAC Address Table (aging after 5') : MAC to reach out to (Source MAC from a received frame) <-> Switch Interface
* FLOOD for Unknown Unicast Frames
* FORWARD for Known Unicast Frames

#### Switches CLI commands
* `show mac address-table`
* `clear mac address-table dynamic address <MAC-address>`
* `clear mac address-table dynamic interface <interface-id>`
* `show ip interface brief`
* `(config) #interface f0/1` -> `(config-if)#speed 100` -> `(config-if)#duplex full` -> `(config-if)#description ## to R1 ##`
* or `(config) #interface range f0/5 - 12` -> `(config-if-range)#description ## not in use ##` -> `(config-if-range)#shutdown`
* or `(config) #interface range f0/5 - 6, f0/9 - 12` -> `(config-if-range)#no shutdown`
* `show interfaces f0/0`
    * Interfaces errors:
        * `runts`: Frames that are smaller than the minimum frame size (64 bytes)
        * `giants`: Frames that are larger than the maximum frame size (1518 bytes)
        * `CRC`: Frames that failed the CRC check (trailer/FCS)
        * `frame` : Frames that have an incorrect format (due to an error)
        * `input errors`: Total of various counters, such as the above four
        * `output errors`: Frames the switch tried to send, but failed due to an error
* `show interfaces description`
* `show interfaces status`

## Routers (Layer 3)
* have fewer network interfaces than switches.
* provide connectivity between LANs.
* Tx: 1+2
* Rx: 3+6
* Auto-MDIX / RJ45 for UTP cables.
* SFP Tranceiver for fiber-optic cables.
* `load-balance` between paths
* use a group of paths as main paths and another group as backup paths.

#### Routers CLI commands
* `show ip interface brief`
* `(config) #interface g0/0` -> `(config-if)#ip address <ip-address-connected-to-interface> <netmask>` assigns an address to the interface -> `(config-if)#no shutdown` -> `(config-if)#description ## to SW1 ##`
* `show interfaces g0/0`
    * Interfaces errors:
        * `runts`: Frames that are smaller than the minimum frame size (64 bytes)
        * `giants`: Frames that are larger than the maximum frame size (1518 bytes)
        * `CRC`: Frames that failed the CRC check (trailer/FCS)
        * `frame` : Frames that have an incorrect format (due to an error)
        * `input errors`: Total of various counters, such as the above four
        * `output errors`: Frames the switch tried to send, but failed due to an error
* `show interfaces description`
* `show ip route`
    * `L` - Local is a route to the actual IP address configured on the interface (/32)
    * `C` - Connected is a route to the network the interface is connected to.
    * `S` - Static is a route that is manually configured to the routes table.
* `ip route <network-IP-address> <netmask> <next-hope-IP-address>`, i.e. ip route 192.168.4.0 255.255.255.0 192.168.13.3
* `ip route <network-IP-address> <netmask> <exit-interface>`, i.e. ip route 192.168.4.0 255.255.255.0 g0/0 (These routes rely on a feature called Proxy ARP to function)
* `ip route <network-IP-address> <netmask> <exit-interface> <next-hope-IP-address>`, i.e. ip route 192.168.4.0 255.255.255.0 g0/0 192.168.13.3
* `ip route 0.0.0.0 0.0.0.0 <IP-address-to-Internet>`, this creates a default route from a router to the Internet (Gateway of last resort)

## End-Hosts (Clients/Servers)
* Define gateway (router)
* Default gateway is 0.0.0.0/0


## Firewalls  (Layer 4?)
* monitor and control network traffic based on configured rules.
* can be placed either inside or outside of the network.
* Tx: 1+2
* Rx: 3+6
* Auto-MDIX / RJ45 for UTP cables.
* SFP Tranceiver for fiber-optic cables.


## Cisco IOS CLI
* RJ45 port (use a rollover cable) 1 <-> 8, 2 <-> 7, 3 <-> 6, 4 <-> 5
* USB Mini-B
* Speed (baud): 9600 bps
* Data bits: 8
* Stop bits: 1
* Parity: None
* Flow control: None
* `running-config` is the current, active configuration file on the device. As you enter commands in the CLI, you edit the active configuration.
* `startup-config` is the configuration file that will be loaded upon restart of the device.
* `Enter` -> enter in USER EXEC MODE `>`
* `enable` -> enter in PRIVILEGED EXEC MODE `#`
* `?` -> view available commands
* `configure terminal`-> enter in GLOBAL CONFIGURATION MODE `(config) #`
* `exit`
* `(config) #enable password <password>` (passwords are case-sensitive, creates a password to enter in `#`)
* `(config) #do show running-config`
* `#write` or `#write memory` or `#copy running-config startup-config`
* `(config) #service password-encryption` -> Type 7 Cisco Password (salted XOR). Not safe - [Decrypt here](https://www.firewall.cx/cisco/cisco-routers/cisco-type7-password-crack.html)
* `(config) #enable secret <password>` -> Type 5 Cisco Password (MD5).
* `(config) #no service password-encryption` -> Cancels T7 encryption for future passwords
* `show mac address-table`
* `clear mac address-table dynamic address <MAC-address>`
* `clear mac address-table dynamic interface <interface-id>`
* `show ip interface brief`
* `(config) #interface g0/0` -> `(config-if)#ip address <ip-address-connected-to-interface> <netmask>` -> `(config-if)#no shutdown` -> `(config-if)#description ## to SW1 ##`
* `show interfaces g0/0`
    * Interfaces errors:
        * `runts`: Frames that are smaller than the minimum frame size (64 bytes)
        * `giants`: Frames that are larger than the maximum frame size (1518 bytes)
        * `CRC`: Frames that failed the CRC check (trailer/FCS)
        * `frame` : Frames that have an incorrect format (due to an error)
        * `input errors`: Total of various counters, such as the above four
        * `output errors`: Frames the switch tried to send, but failed due to an error
* `show interfaces description`
* `show interfaces status`

## Node-to-Node Communication

#### 1. PCs + Switches
* LAN: 192.168.1.0/24
* Architecture:
    * (0C.2F.B0.11.9D.00) PC1 (.1) <-> (G0/0) SW1 (G0/2) <-> (G0/2) SW2 (G0/0) <-> (0C.2F.B0.6A.39.00) PC3 (.3)
* Scenario: We want to `PING` PC3 from PC1, but PC1 only knows the IP address of PC3. Not the MAC address.
* Process:
    * `ARP Cycle`
        * PC1 will send in SW1 an `ARP Request`
            * Src IP: 192.168.1.1
            * Dst IP: 192.168.1.3
            * Src MAC: .9D00
            * Dst MAC: FF.FF.FF.FF.FF.FF
        * SW1 will `BROADCAST` the `ARP Request` and add the MAC address .9D00 in its MAC address table
            * .9D00 <--> G0/0
        * SW2 will `BROADCAST` the `ARP Request` and add the MAC address .9D00 in its MAC address table
            * .9D00 <--> G0/2
        * PC3 will send in SW2 an `ARP Reply`
            * Src IP: 192.168.1.3
            * Dst IP: 192.168.1.1
            * Src MAC: .3900
            * Dst MAC: .9D00
        * SW2 will `FORWARD` the `ARP Reply` and add the MAC address .3900 in its MAC address table
            * .9D00 <--> G0/2
            * .3900 <--> G0/0
        * SW1 will `FORWARD` the `ARP Reply` and add the MAC address .3900 in its MAC address table
            * .9D00 <--> G0/0
            * .3900 <--> G0/2
        * PC1 receives the `ARP Reply`
    * `ICMP Cycle`
        * PC1 creates the `ICMP Echo Request` (which is a PING frame)
            * Src IP: 192.168.1.1
            * Dst IP: 192.168.1.3
            * Src MAC: .9D00
            * Dst MAC: .3900

            and `FORWARD` it to SW1
        * SW1 `FORWARD` the frame to SW2
        * SW2 `FORWARD` the frame to PC3
        * PC3 creates the `ICMP Echo Reply` and `FORWARD` it to SW2
        * SW2 `FORWARD` it to SW1
        * SW1 `FORWARD` it to PC1
        * Future pings will happens without the necessity of the ARP communication - as long as less than 5' apart.

#### 2. PCs + Switches + Routers
* WAN
    * LAN1  :   192.168.1.0/24      : PC1 (192.168.1.1, g0/0, 1111) + Switch (g0/1, g0/0) + R1 (192.168.1.254, g0/2, aaaa)
    * LAN12 :   192.168.12.0/24     : R1 (192.168.12.1, g0/0, bbbb) + R2 (192.168.12.2, g0/0, cccc)
    * LAN13 :   192.168.13.0/24     : R1 (192.168.13.1, g0/1) + R3 (192.168.13.3, g0/1)
    * LAN24 :   192.168.24.0/24     : R2 (192.168.24.2, g0/1, dddd) + R4 (192.168.24.4, g0/1, eeee)
    * LAN34 :   192.168.34.0/24     : R3 (192.168.34.3, g0/0) + R4 (192.168.34.4, g0/0)
    * LAN4  :   192.168.4.0/24      : PC4 (192.168.4.1, g0/0, 4444) + Switch (g0/1, g0/0) + R4 (192.168.4.254, g0/2, fffe)
* Process: PC1 --> PC4 communication through R2
    * PC1 BROADCAST an ARP Request asking for R1's MAC address.
    * R1 UNICAST an ARP Reply to PC1
    * Packet: PC1 <--> R1
        * L3 Header
            Src IP : 192.168.1.1
            Dst IP : 192.168.4.1
        * L2 Header
            Src MAC: 1111
            Dst MAC: aaaa
    * R1 BROADCAST an ARP Request asking for R2's MAC address.
    * R1 <--> R2
        * L3 Header
            Src IP : 192.168.1.1
            Dst IP : 192.168.4.1
        * L2 Header
            Src MAC: bbbb
            Dst MAC: cccc
    * R2 BROADCAST an ARP Request asking for R4's MAC address.
    * R2 <--> R4
        * L3 Header
            Src IP : 192.168.1.1
            Dst IP : 192.168.4.1
        * L2 Header
            Src MAC: dddd
            Dst MAC: eeee
    * R4 BROADCAST an ARP Request asking for PC4's MAC address.
    * R4 <--> PC4
        * L3 Header
            Src IP : 192.168.1.1
            Dst IP : 192.168.4.1
        * L2 Header
            Src MAC: fffe
            Dst MAC: 4444

## Subnetting
* CIDR = Classless Inter-Domain Routing ---> Prefix notation different from /8, /16, /24

* Class C (/24) Subnetting CIDR Notation
  Prefix        # Subnets       # Hosts/subnet          Netmask
    /25               2              126            255.255.255.128  (255-127)
    /26               4               62            255.255.255.192  (255-63)    i.e. x.x.x.0/26, x.x.x.64/26, x.x.x.128/26, x.x.x.192/26
    /27               8               30            255.255.255.224  (255-31)    i.e. x.x.x.0/27, x.x.x.32/27, x.x.x.64/27, x.x.x.96/27, ...
    /28              16               14            255.255.255.240  (255-15)
    /29              32                6            255.255.255.248  (255-7)
    /30              64                2            255.255.255.252  (255-3)
    /31             128                0 (2)
    /32             256                0 (1)

* Class B (/16) Subnetting CIDR Notation
  Prefix        # Subnets       # Hosts/subnet
    /17               2             32766
    /18               4             16382
    /19               8              8190
    /20              16              4094
    /21              32              2046
    /22              64              1022
    /23             128               510   i.e. x.x.0.0/23, x.x.2.0/26, x.x.4.0/26, x.x.8.0/26, x.x.16.0/26, ...
    /24             256               254
    /25             512               126
    /26            1024                62
    /27            2048                30
    /28            4096                14
    /29            8192                 6
    /30           16384                 2
    /31           32768                 0 (2)
    /32           65536                 0 (1)

* Class A (/8) Subnetting CIDR Notation
  Prefix        # Subnets       # Hosts/subnet
    /9                 2             8388606
    /10                4             4194302
    /11                8             2097150
    /12               16             1048574
    /13               32              524286
    /14               64              262142
    /15              128              131070
    /16              256               65534
    /17              512               32766
    /18             1024               16382
    /19             2048                8190
    /20             4096                4094
    /21             8192                2046
    /22            16384                1022
    /23            32768                 510
    /24            65536                 254
    /25           131072                 126
    /26           262144                  62
    /27           524288                  30
    /28          1048576                  14
    /29          2097152                   6
    /30          4194304                   2

Example: We have the following network architecture:

* LAN1 includes PC1, SW1 and R1(g0/0). This subnet should be able to have maximum 45 hosts
* LAN2 includes PC2, SW2 and R1(g0/1). This subnet should be able to have maximum 64 hosts
* LAN3 includes PC3, SW3 and R2(g0/0). This subnet should be able to have maximum 14 hosts
* LAN4 includes PC4, SW4 and R2(g0/1). This subnet should be able to have maximum 9 hosts
* P2P includes R1(g0/0/0) and R2(g0/0/0)

1. Subnet the 192.168.5.0/24 network to provide sufficient addressing for each LAN. (Also, the point-to-point connection between R1 and R2).
* LAN2 192.168.5.0/25
    * Network       :   192.168.5.0/25
    * Broadcast     :   192.168.5.127/25
* LAN1 192.168.5.128/26
    * Network       :   192.168.5.128/26
    * Broadcast     :   192.168.5.191/26
* LAN3 192.168.5.192/28
    * Network       :   192.168.5.192/28
    * Broadcast     :   192.168.5.207/28
* LAN4 192.168.5.208/28
    * Network       :   192.168.5.208/28
    * Broadcast     :   192.168.5.223/28
* P2P 192.168.5.224/30
    * Network       :   192.168.5.224/30
    * Broadcast     :   192.168.5.227/30

2. Assign the first usable address to the PC in each LAN.
* PC1       :   192.168.5.129/26 (255.255.255.192)
* PC2       :   192.168.5.1/25   (255.255.255.128)
* PC3       :   192.168.5.193/28 (255.255.255.240)
* PC4       :   192.168.5.209/28 (255.255.255.240)

3. Assign the last usable address to the router's interface in each LAN.
* R1 g0/0   :   192.168.5.190/26 (255.255.255.192)
* R1 g0/1   :   192.168.5.126/25 (255.255.255.128)
* R1 g0/0/0 :   192.168.5.225/30 (255.255.255.252)
* R2 g0/0   :   192.168.5.206/28  (255.255.255.240)
* R2 g0/1   :   192.168.5.222/28 (255.255.255.240)
* R2 g0/0/0 :   192.168.5.226/30 (255.255.255.252)

4. Configure static routes on each router so that all PCs can ping each other.
* Configure PCs assigning the appropriate IPv4 addresses and setting the proper Router interface as default gateway.
* R1 configuration:
    * enable
    * configure terminal
    
    * interface g0/1
    * ip address 192.168.5.126 255.255.255.128
    * no shutdown
    * do show ip interface g0/1
    
    * interface g0/0
    * ip address 192.168.5.190 255.255.255.192
    * no shutdown
    * do show ip interface g0/0
    
    * interface g0/0/0
    * ip address 192.168.5.225 255.255.255.252
    * no shutdown
    * do show ip interface g0/0/0
* R2 configuration:
    * enable
    * configure terminal
    
    * interface g0/1
    * ip address 192.168.5.222 255.255.255.240
    * no shutdown
    * do show ip interface g0/1
    
    * interface g0/0
    * ip address 192.168.5.206 255.255.255.240
    * no shutdown
    * do show ip interface g0/0
    
    * interface g0/0/0
    * ip address 192.168.5.226 255.255.255.252
    * no shutdown
    * do show ip interface g0/0/0



'e'.join('nvr')
'annog'[::-1]
'forgive'[-4:]
('me', 'you')[1]
'soup'.split('o')[1]
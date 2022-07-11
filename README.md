## Problem Statement

A small business organization consisting of a few servers like web servers, backup servers, database servers and host machines needs to monitor and inspect the data packets travelling along its network to detect anomalies, monitor network usage and analyze the traffic. They also want to make sure all the employee is accessing only work-related websites. For this purpose, they need to implement a sniffer in their data center.

## Introduction
A network sniffer “sniffs” or monitors network traffic for information like where it’s coming from, which device, the protocol used, etc. This information can help network administrators to find security holes in their environment and thus optimize it. However, a common use for them today lies in black hat hacking. In the wrong hands, network sniffing tools can allow anyone with little to no hacking skills to monitor network traffic over unsecured WiFi networks to steal passwords and other private information. In this project, we tried to mimic a real-world scenario in which we took a small business set up with a few servers and host machines. One of the hosts acted as the sniffer in this setup for which we ran some tests to verify the same.

## Working of a Sniffer
Sniffers work by examining streams of data packets that flow between computers on a network as well as between networked computers and the larger Internet. Networks function as a collection of nodes, such as your smartphone, laptop, server, etc., which transfer information over a networked connection. To speed these transfers along their route, networks use packets of data—chunks of data that are broken down and then reassembled after the transmission is complete—to help avoid network congestion. By using network sniffers to “sniff” the packets en route, a user can analyze the traffic via passive sniffing i.e., snooping in on the inflight data or active sniffing that is directly interacting by sending packets and receiving responses from the target devices. The latter unfortunately also allows for cybercrime instances. Using encrypted protocols can help prevent unauthorized network sniffing to an extent.

## Network Topology

![topology](./images/Network%20Diagram%20-%20design%20new.png)

Figure 1 shows the topology design for our business case. It consists of 10 switches and 12 hosts. The figure also shows the port to which each device is connected. Switch S1 is connected to the webserver and switch S2 to the backup server. We made H3 our data server as a sniffer machine so that it will sniff all the packets passing via switch S3. Switches 4 and 5 are the main switches that are connecting different departments. This small company has 5 departments, Accounts, IT, Sales, Marketing and service delivery. 

## Topology in Flow Manager

 
![TOPOLOGY IN FLOW MANAGER](./images/Flow%20Manager%20Topology%20Diagram.png)

## Technical Details

The first step in our project was to design a topology that best suits our business scenario. In our design, we had 10 switches and 12 hosts. The ports are accurately connected to switches with no same port linked to two hosts or switches. The topology file is coded in python. We also implemented flows for the switches. Executing the following Mininet code creates the topology depicted in figure 2.

### Flows

The flows for the switch 3 which is connected to the sniffer are as below:
![flow in switch3](./images/Flow1%20in%20sniffer%20S3.png)
 
![FLOW1 IN SWITCH S3](./images/Flow%202%20in%20sniffer.png)


As we can understand from the flows, for switch 3 all the packets received from port2 will be forwarded to Group table2(Group table ID 51). Similarly, flow 2 for switch 3 has match as in_port 3 and action to the group table 50. That is all the packets received from port3 will be forwarded to Group table1(Group table ID 50). Moreover, we created flows for all the switches in the topology.

There are 2 group tables with group_id 50 and 51. The type is defined as ALL group, which will take any packet received as input and duplicate it to be operated on independently by each bucket in the bucket list. In this way, an ALL group can be used to replicate and then operate on separate copies of the packet defined by the actions in each bucket.
 
For Group table1(Group Table ID 50), we created two buckets - one bucket will send the packet to Port1, and another bucket will send the packet to Port2. Similarly, for Group table2(Group ID 51) we created two buckets - one bucket will send the packet to Port3, and another bucket will send the packet to Port1.

## Steps 

* Run the topology file 
sudo python2 topology.py
* Run the ryu controller application(simple switch and ofctl)
ryu-manager ryu.app.simple_switch_13 ryu.app.ofctl_rest
* Do pingall from mininet
* Check the flows of switch s3
 sudo ovs-vsctl show
 sudo ovs-ofctl -O OpenFlow13 dump-flows s3 
sudo ovs-ofctl -O OpenFlow13 dump-groups s3
* Configure the Group in S2
curl -X POST http://localhost:8080/stats/groupentry/add -d '@group50.json' 
curl -X POST http://localhost:8080/stats/groupentry/add -d '@group51.json'
* Check the group tables.
* Configure all the Flows. Here just showing only for switch S3 connected to the sniffer. Similarly, add the flowings for all the remaining ones and check the flow tables.
curl -X POST http://localhost:8080/stats/flowentry/add -d '@s3_flow1.json' 
curl -X POST http://localhost:8080/stats/flowentry/add -d '@s3_flow2.json'
 * Testing
Trigger a continuous ping from h1 to h12 and capture traffic in h3 using tcpdump
 a) start the xterm for h3
 In the h3 terminal capture tcpdump 
 tcpdump -i any icmp -vvv
 b) continuous ping from h1 to h12
 c) check the h3 xterm window, you will observe the h1 to h12 traffic.

 ![XTERM IN H3](./images/4%20Sniffer%20in%20H3.png)

#! /usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class ProjectTopo(Topo):
	def build(self):
		# Adding the switches
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		s10 = self.addSwitch('s10')
		
		# Adding hosts
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		h8 = self.addHost('h8')
		h9 = self.addHost('h9')
		h10 = self.addHost('h10')
		h11 = self.addHost('h11')
		h12 = self.addHost('h12')
		
		# Adding the links
		self.addLink(s1,s2,2,2)
		self.addLink(s2,s3,3,2)
		self.addLink(s3,s4,3,3)
		self.addLink(s4,s5,4,3)
		self.addLink(s4,s6,1,3)
		self.addLink(s4,s7,2,3)
		self.addLink(s5,s8,1,3)
		self.addLink(s5,s9,2,3)
		
		self.addLink(s1,h1,1,1)
		self.addLink(s2,h2,1,1)
		self.addLink(s3,h3,1,1)
		self.addLink(s6,h4,1,1)
		self.addLink(s6,h5,2,1)
		self.addLink(s7,h6,1,1)
		self.addLink(s7,h7,2,1)
		self.addLink(s8,h8,1,1)
		self.addLink(s8,h9,2,1)
		self.addLink(s9,h10,1,1)

		self.addLink(s9,s10,2,1) 
		self.addLink(s10,h11,2,1)
		self.addLink(s10,h12,3,1)
		
if __name__ == '__main__':
	setLogLevel('info')
	topo = ProjectTopo()
	c1 = RemoteController('c1', ip='127.0.0.1')
	net = Mininet(topo=topo, controller=c1)
	net.start()	
	CLI(net)
	net.stop()
		
		


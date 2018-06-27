#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class MyTopo(Topo):
    # Single switch connected to n hosts
    def __init__(self):
        # Initialize topology and default optioe
        Topo.__init__(self)
        h1 = self.addHost('h1',mac='00:00:00:00:00:01')
        h2 = self.addHost('h2',mac='00:00:00:00:00:02')
        h3 = self.addHost('h3',mac='00:00:00:00:00:03')
        h4 = self.addHost('h4',mac='00:00:00:00:00:04')
        s1 = self.addSwitch('s1')

        self.addLink(h1,s1,bw=3)
        self.addLink(h2,s1,bw=10)
        self.addLink(h3,s1,bw=10)
        self.addLink(h4,s1,bw=10)

def startmn():
    "Create network and run simple performance test"
    topo = MyTopo()
    #net = Mininet( topo=topo, controller=RemoteController, host=CPULimitedHost, link=TCLink )
    net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    #print "Testing network connectivity"
    #net.pingAll()
    
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    result = h1.cmd('sudo /opt/lampp/lampp stop')
    #print result
    result = h1.cmd('sudo /opt/lampp/lampp start')
    #print result
    
    result = h2.cmd('firefox -P --no-remote &')
    result = h3.cmd('firefox -P --no-remote &')
    result = h4.cmd('firefox -P --no-remote &')

    CLI(net)
    net.stop()
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    startmn()

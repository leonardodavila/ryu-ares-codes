"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class ProvisioningTopology( Topo ):
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )

        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( host1, switch1 )
        self.addLink( host2, switch2 )
        self.addLink( host3, switch3 )
        self.addLink( switch2, switch3)
        self.addLink( switch1, switch2)


topos = { 'provisioning': ( lambda: ProvisioningTopology() ) }
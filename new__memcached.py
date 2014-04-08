""" 
HINT 1: Run this file first to see how the current implementation of memcache
deals with adding a host.

HINT 2: Browse the python-memcached source code to see how keys are distributed
across multiple servers.

You'll need to setup 8 running memcached instances on the following ports:
11211
11212
11213
11214
11215
11216
11217
11218

Minimum requirements:

apt-get install memcached
python-memcached==1.53
python2.7

You can use any existing python libraries to help you in this task.
"""

import random
import string
import memcache
from hash_ring import *  # @UnusedWildImport

class MemcacheClient(memcache.Client):
    """ A memcache subclass. It currently allows you to add a new host at run
    time. 

    Sadly, this truely messes with the our keys. I.E. Adding a host at runtime
    effectively wipes our cache all together...Wonder why?
    """
    
    def __init__(self, *args, **kwargs):
        super(MemcacheClient, self).__init__(*args, **kwargs)
        self.mc_ring = MemcacheRing(servers)

    
    def _get_server(self, key):
        
        server = self.mc_ring.hash_ring.get_node(key)
        return server, key


    def add_server(self, server):
        """ Adds a host at runtime to client
        """
        # Create a new host entry
        server = memcache._Host(
            server, self.debug, dead_retry=self.dead_retry,
            socket_timeout=self.socket_timeout,
            flush_on_reconnect=self.flush_on_reconnect
        )
        # Add this to our server choices 
        self.servers.append(server)
        self.buckets.append(server)
        self.mc_ring.servers.append(server)
        self.mc_ring.buckets.append(server)
        
        # Create a new host entry
        
        #self.servers.append(server)
        # Update our buckets
        #self.buckets.append(server)


    def ring_info(self,servers):
        print 55*'#'
        print("-> Here's our %s servers:" % len(client.mc_ring.servers))
        count=0
        str_servers = ""
        for server in client.mc_ring.servers:
            str_server="%s:%s" % (server.address[0], server.address[1])
            node_pos = client.mc_ring.hash_ring.get_node_pos(str_server)
            if count < (len(client.mc_ring.servers) - 1):
                str_servers += "# %s => Node_Ring_Position:%s\n" % (str_server,node_pos)
            else:
                str_servers += "# %s => Node_Ring_Position:%s" % (str_server,node_pos)
            count = count + 1
        print 55*'#'
        print(str_servers)
        print 55*'#'

def random_key(size):
    """ Generates a random key
    """
    return ''.join(random.choice(string.letters) for _ in range(size))


if __name__ == '__main__':
    
    # We have 7 running memcached servers
    servers = ['127.0.0.1:1121%d' % i for i in range(1,8)]
    
    # We have 100 keys to split across our servers
    keys = [random_key(10) for i in range(50)]
    
    # Init our subclass
    client = MemcacheClient(servers=servers)
    
    for key in keys:
        client.mc_ring.set(key, 1)
    
    # Getting ring info
    client.ring_info(servers)
    
    # Check how many keys come back 
    valid_keys = client.mc_ring.get_multi(keys)
    print '%s percent of keys matched' % ((len(valid_keys)/float(len(keys))) * 100)
    print 55*'#'

    print 'Added new server' 
    
    # Adding another server at run time
    client.add_server('127.0.0.1:11218')
    client.add_server('127.0.0.1:11219')
    client.add_server('127.0.0.1:11220')
    client.add_server('127.0.0.1:11221')
    
    # Getting ring info
    client.ring_info(servers)
    
    valid_keys = client.mc_ring.get_multi(keys)
    print '%s percent of keys stil matched' % ((len(valid_keys)/float(len(keys))) * 100)
    print 55*'#'
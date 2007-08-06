from twisted.protocols.jabber import client, jid
from twisted.protocols import xmlstream
from twisted.xish import domish
from twisted.internet import reactor
import config

class wrapper:
 def __init__():
  self.jid = jid.Jid("%s@%s/%s" % (config.USER, config.SERVER, config.RESOURCE))
  self.c = client.basicClientFactory(self.jid, config.PASSWD)
reactor.connectTCP(server, 5222, factory) 
reactor.run()

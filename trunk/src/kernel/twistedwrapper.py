from twisted.words.protocols.jabber import client, jid, xmlstream
#from twisted.protocols import xmlstream
from twisted.xish import domish
from twisted.internet import reactor
import config

class wrapper:
 def __init__(self):
  self.jid = jid.Jid("%s@%s/%s" % (config.USER, config.SERVER, config.RESOURCE))
  self.c = client.basicClientFactory(self.jid, config.PASSWD)
  self.c.addBootstrap(xmlstream.NS_AUTHD_EVENT, self.authd);
  self.x=None
  reactor.connectTCP(config.SERVER, 5222, self.c) 
  reactor.run()
 def authd(self, x):
  self.x=x;
  print "Authenticated.. %s" % (self.jid, );


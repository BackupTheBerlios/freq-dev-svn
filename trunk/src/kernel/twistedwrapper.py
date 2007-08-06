from twisted.words.protocols.jabber import client, jid, xmlstream
from twisted.words.xish import domish
from twisted.internet import reactor
import config

class wrapper:
 def __init__(self):
  self.jid = jid.JID("%s@%s/%s" % (config.USER, config.SERVER, config.RESOURCE))
  self.c = client.basicClientFactory(self.jid, config.PASSWD)
  self.c.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, self.authd);
  self.x=None
  reactor.connectTCP(config.SERVER, 5222, self.c) 
  reactor.run()
 def authd(self, x):
  self.x=x;
  print "Authenticated.."
  p=domish.Element(("jabber:client", "presence"))
  p.addElement("status").addContent("some status")
  p.addElement("show").addContent("chat")
  self.x.send(p)
  self.x.addObserver("/*", self.cb);
 def cb(self, x):
  #<debug lines>
  print "stanza: "+x.toXml()
  #</debug lines>
 

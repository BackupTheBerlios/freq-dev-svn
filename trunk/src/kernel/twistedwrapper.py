from twisted.words.protocols.jabber import client, jid, xmlstream
from twisted.words.xish import domish
from twisted.internet import reactor
import config

class wrapper:
 def __init__(self):
  self.jid = jid.JID("%s@%s/%s" % (config.USER, config.SERVER, config.RESOURCE))
  self.c = client.basicClientFactory(self.jid, config.PASSWD)
  self.c.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, self.authd);
  self.x = None
  self.handlers = []
  reactor.connectTCP(config.SERVER, 5222, self.c) 
  reactor.run()
 def getChild(self, x, n):
  y=[i for i in x.Children if i.name=y][0]
  return y
 def authd(self, x):
  self.x=x;
  print "Authenticated.."
  p=domish.Element(("jabber:client", "presence"))
  p.addElement("status").addContent("some status")
  p.addElement("show").addContent("chat")
  self.x.send(p)
  #self.x.send("<message to='freq2@burdakov.pp.ru'/>")   ## debug
  self.x.addObserver("/*", self.cb);
 def cb(self, x):
  n=x.name
  try: id=x["id"]
  except: id="something"
  try: typ=x["type"]
  except: typ="none"
  try: body=self.getChild(x, "body").getContent()
  except: body=''
  try: f=x["from"]
  except: f=""
  for i in self.handlers:
   if (i[0] in (n, None)) and (i[1] in (typ, None)) and (i[2] in (id, None)) and (i[3] in (body, None)) and (i[4] in (f, None)):
    i[5](x);
 def register_handler(func, stanza=None, typ=None, id=None, body=None, f=None):
  self.handlers.add((stanza, typ, id, body, f, func))

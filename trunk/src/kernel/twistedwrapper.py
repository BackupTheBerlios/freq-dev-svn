from twisted.words.protocols.jabber import client, jid, xmlstream
from twisted.words.xish import domish
from twisted.internet import reactor
from twisted.web.html import escape
import traceback
import re
import log
import sys
import config

class wrapper:

 def __init__(self):
  self.tc = 0
  self.jid = jid.JID("%s@%s/%s" % (config.USER, config.SERVER, config.RESOURCE))
  self.onauthd = None
  self.c = client.basicClientFactory(self.jid, config.PASSWD)
  self.c.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, self.authd);
  self.x = None
  self.log = log.logger()
  self.handlers = []
  self.msghandlers = []
  reactor.connectTCP(config.SERVER, 5222, self.c) 
 
 def getChild(self, x, n):
  return [i for i in x.children if (i.__class__==domish.Element) and (i.name==n)][0]
 
 def authd(self, x):
  self.x = x
  print 'Authenticated'
  p = domish.Element(("jabber:client", "presence"))
  p.addElement("status").addContent(config.STATUS)
  p.addElement("show").addContent("chat")
  self.x.send(p)
  self.x.addObserver("/*", self.cb)
  self.x.addObserver("/message", self.cbmessage)
  self.onauthd()
 
 def cb(self, x):
  n = x.name
  try: id = x["id"]
  except: id = "something"
  try: typ = x["type"]
  except: typ = ''
  try: body = self.getChild(x, "body").children[0]
  except: body = ''
  f = x["from"]
  for i in self.handlers:
   if (i[0] in (n, None)) and (i[1] in (typ, None)) and (i[2] in (id, None)) and (i[3] in (body, None)) and (i[4] in (f, None)):
    if i[6]: self.handlers.remove(i)
    reactor.callInThread(self.call, i[5], x);
 
 def register_handler(self, func, stanza=None, typ=None, id=None, body=None, f=None, once=None):
  self.handlers.append((stanza, typ, id, body, f, func, once))
 
 def register_msg_handler(self, func, body, typ=None, f=None):
  self.msghandlers.append((func, body, typ, f))
 
 def cbmessage(self, x):
  delayed = [i for i in x.children if (i.__class__==domish.Element) and ((i.name=='delay') or ((i.name=='x') and (i.uri=='jabber:x:delay')))]
  try: body = self.getChild(x, 'body').children[0]
  except: body = ''
  f = x['from']
  try: typ = x['type']
  except: typ = 'chat'
  for i in self.msghandlers:
   if re.search(i[1], body, re.DOTALL) and (i[2] in (typ, None)) and (i[3] in (f, None)) and not delayed:
    reactor.callInThread(self.call, i[0], typ, f, body)
 
 def send(self, x):
  self.log.log(u'try to send stanza to %s..' % (x['to'], ), 1)
  reactor.callFromThread(self.x.send, x)
 
 def msg(self, typ, j, body, subject=None):
  m = domish.Element(("jabber:client", "message"))
  m["type"] = typ
  m["to"] = j
  m.addElement("body").addContent(body)
  if subject: m.addElement("subject").addContent(subject)
  self.send(m)
 
 def call(self, f, *args, **kwargs):
  try:
   self.tc = self.tc + 1
   self.log.log('== started thread #%s: %s', (self.tc, f), 1)
   f(*args, **kwargs)
   self.log.log('== finished thread #%s: %s', (self.tc, f), 1)
  except:
   m = "".join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
   print "STOP: ", m
   self.log.err(escape(m))
   self.log.err('=^ failed thread #%s' % (self.tc, ))
   reactor.stop()

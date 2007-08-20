import twisted
from twisted.internet import reactor
from twisted.web.html import escape
from twisted.words.xish import domish
from item import item as new_item
from twistedwrapper import wrapper
from pluginloader import pluginloader
from muc import muc
import config
if config.ENABLE_SQLITE: import db
import time
import os
import sys
import lang
import log


class freqbot:

 def __init__(self, q):
  self.version_name = u'freQ'
  self.version_version = u'1.0.0'+self.getRev()
  self.version_os = u'Twisted %s, Python %s' % (twisted.__version__, sys.version)
  self.wrapper = wrapper()
  self.wrapper.onauthd = self.onauthd
  self.wrapper.register_handler(self.iq_handler, 'iq', 'get')
  self.wrapper.c.addBootstrap('//event/client/basicauth/authfailed', self.failed)
  self.wrapper.c.addBootstrap('//event/client/basicauth/invaliduser', self.failed)
  print "ok"
  self.g = {}
  self.alias_engine = None
  self.plug = pluginloader(self, q)
  self.muc = muc(self)
  self.log = log.logger()
  self.log.log('freQ %s started with pid=%s' % (self.version_version, os.getpid()))
  self.cmdhandlers = []
  if config.ENABLE_SQLITE: self.db = db.db()
  self.wrapper.register_msg_handler(self.call_cmd_handlers, u".*")
 
 def failed(self, x):
  print 'connect failed!'
  self.log.err('cannot login to jabber account (eg invalid username/password ) :(')
  reactor.stop()
  
 def register_cmd_handler(self, func, cmd, required_access=0, g=None):
  self.cmdhandlers.append((func, cmd, required_access, g))
 
 def call_cmd_handlers(self, t, s, b):
  groupchat = s.split("/")[0]
  b = self.alias_engine(groupchat, b)
  params = b.split()
  nick = s[len(groupchat)+1:]
  try: item = self.g[groupchat][nick]
  except:
   item = new_item(self)
   item.jid = s
   item.realjid = s
  if len(params):
   cmd = b.split()[0]
   params = b[len(cmd)+1:]
   for i in self.cmdhandlers:
    if cmd.lower() == i[1]:
     if item.allowed(i[2]):
      if item.room or not i[3]: i[0](t, item, params)
      else: item.lmsg(t, "muc_only")
     else: item.lmsg(t, "not_allowed")
 
 def onauthd(self):
  groupchats = self.muc.load_groupchats()
  for i in groupchats: self.muc.join(i)
  print "Joined %s groupchats" % len(groupchats, )
 
 def read_file(self, fn):
  f = file(fn, "r")
  content = f.read().decode("utf8")
  f.close()
  return content
 
 def iq_handler(self, x):
  for child in x.children:
   if (child.__class__==domish.Element) and (child.name=='query') and (child.uri=='jabber:iq:version'):
    answer = domish.Element(('jabber:client', 'iq'))
    answer['type'] = 'result'
    answer['id'] = x.getAttribute('id')
    answer['to'] = x.getAttribute('from')
    query = answer.addElement('query', 'jabber:iq:version')
    query.addElement('name').addContent(self.version_name)
    query.addElement('version').addContent(self.version_version)
    query.addElement('os').addContent(self.version_os)
    self.log.log(escape(u'version request: %s\nAnswer: %s' % (x.toXml(), answer.toXml())), 2)
    self.wrapper.send(answer)
 
 def getRev(self):
  try:
   p = os.popen(config.SVNVERSION)
   time.sleep(1)
   r = p.read()
   if r: r = '.r'+r
   return r
  except: return '' 

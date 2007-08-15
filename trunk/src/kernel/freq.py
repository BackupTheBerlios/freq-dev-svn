import config
import time
import os
import twisted
import sys
from twisted.web.html import escape
from twisted.words.xish import domish
from item import item as new_item
from twistedwrapper import wrapper
from pluginloader import pluginloader
from muc import muc
if config.ENABLE_SQLITE: import db
import lang
import log

class freqbot:
 def __init__(self, q):
  self.version_name = u'freQ'
  self.version_version = u'0.2.0'+self.getRev()
  self.version_os = u'Twisted %s, Python %s' % (twisted.__version__, sys.version)
  self.wrapper = wrapper()
  self.wrapper.onauthd = self.onauthd
  self.wrapper.register_handler(self.iq_handler, 'iq', 'get')
  print "wrapper initialized"
  self.g = {}
  self.plug = pluginloader(self, q)
  self.muc = muc(self)
  self.log = log.logger()
  self.log.log('freQ %s started with pid=%s' % (self.version_version, os.getpid()))
  self.cmdhandlers = []
  if config.ENABLE_SQLITE: self.db = db.db()
  self.wrapper.register_msg_handler(self.call_cmd_handlers, u".*")
 def register_cmd_handler(self, func, cmd, required_access=0, g=None):
  self.cmdhandlers.append((func, cmd, required_access, g))
 def call_cmd_handlers(self, t, s, b):
  params = b.split()
  groupchat = s.split("/")[0]
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
  for i in self.muc.load_groupchats(): self.muc.join(i)
  print "Joined groupchats"
 def read_file(self, fn):
  f = file(fn, "r")
  content = f.read().decode("utf8")
  f.close()
  return content
 def iq_handler(self, x):
  for child in x.children:
   if (child.name=="query") and (child.uri=="jabber:iq:version"):
    answer = domish.Element(("jabber:client", "iq"))
    answer["type"] = "result"
    answer["id"] = x.getAttribute("id")
    answer["to"] = x.getAttribute("from")
    query = answer.addElement("query")
    query.uri = "jabber:iq:version"
    query.defaultUri = query.uri
    query.addElement("name").addContent(self.version_name)
    query.addElement("version").addContent(self.version_version)
    query.addElement("os").addContent(self.version_os)
    self.log.log(escape(u"version request: %s\nAnswer: %s" % (x.toXml(), answer.toXml())), 2)
    self.wrapper.send(answer)
 def getRev(self):
  try:
   p = os.popen(config.SVNVERSION)
   time.sleep(1)
   r = p.read()
   if r: r = '.r'+r
   return r
  except: return '' 

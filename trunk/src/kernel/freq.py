from twistedwrapper import wrapper
from pluginloader import pluginloader
from muc import muc
import db
import lang
import log

class freqbot:
 def __init__(self, q):
  self.wrapper=wrapper()
  self.wrapper.onauthd = self.onauthd
  print "wrapper initialized"
  self.g={}
  self.plug=pluginloader(self, q)
  self.muc=muc(self)
  self.log=log.logger()
  self.log.log("bot started")
  self.cmdhandlers = []
  self.db=db.db()
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
    if cmd.lower()==i[1]:
     if self.muc.allowed(s, i[2]):
      if item.room or not i[3]: i[0](t, item, params)
      else: item.lmsg(t, "muc_only")
     else: item.lmsg(t, "not_allowed")
 def onauthd(self):
  for i in self.muc.load_groupchats(): self.muc.join(i)
  print "joined to groupchats"
 def read_file(self, fn):
  f = file(fn, "r")
  content = f.read().decode("utf8")
  f.close()
  return content


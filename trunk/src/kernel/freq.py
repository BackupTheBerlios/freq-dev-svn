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
 def register_cmd_handler(self, func, cmd, required_access=0):
  self.cmdhandlers.append((func, cmd, required_access))
 def call_cmd_handlers(self, t, s, b):
  params=b.split()
  if len(params):
   cmd=params[0]
   params = b[len(cmd):].strip()
   for i in self.cmdhandlers:
    if cmd.lower()==i[1]:
     if self.muc.allowed(s, i[2]): i[0](t, s, params)
     else: self.muc.msg(t, s, lang.msg("not_allowed", l=lang.getLang(s)))
 def onauthd(self):
  for i in self.muc.load_groupchats(): self.muc.join(i)


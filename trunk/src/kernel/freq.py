from twistedwrapper import wrapper
from pluginloader import pluginloader
from muc import muc
import lang
import log

class freqbot:
 def __init__(self, q):
  self.wrapper=wrapper();
  print "wrapper initialized"
  self.g={}
  self.plug=pluginloader(self, q)
  self.muc=muc(self)
  self.log=log.logger()
  self.log.log("bot started")
  self.cmdhandlers = []
 def register_cmd_handler(self, func, cmd, required_access=0):
  self.cmdhandlers.append((func, cmd, required_access))
 def call_cmd_handlers(self, t, s, b):
  params=b.split()
  if len(params):
   cmd=params[0]
   params=params[1:]
   for i in self.cmdhandlers:
    if cmd.lower()==i[1]:
     if bot.muc.allowed(s, required_access): i[0](t, s, params)
     else: bot.muc.msg(t, s, lang.msg("not_allowed", l=lang.getLang(s)))


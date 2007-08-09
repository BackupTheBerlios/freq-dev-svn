import lang
import time

class item:
 def __init__(self, bot, room=None):
  self.bot = bot
  self.handled = None
  self.room = room
  self.jid = None
  self.realjid = None
  self.nick = None
  self.role = None
  self.affiliation = None
  self.joined = time.time()
 def msg(self, typ, body):
  self.bot.muc.msg(typ, self.jid, body)
 def lmsg(self, typ, template, *params):
  self.bot.muc.msg(typ, self.jid, lang.msg(template, params, lang.getLang(self.jid)))


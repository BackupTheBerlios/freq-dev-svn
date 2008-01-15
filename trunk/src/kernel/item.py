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
  self.status = None
  self.show = None

 def msg(self, typ, body):
  if (typ=='groupchat') and self.room and (len(body)>self.room.get_msglimit()):
   self.bot.muc.msg(typ, self.jid, lang.msg('see_private', l=lang.getLang(self.jid)))
   typ = 'chat'
  self.bot.muc.msg(typ, self.jid, body)

 def lmsg(self, typ, template, *params):
  self.msg(typ, lang.msg(template, params, lang.getLang(self.jid)))

 def syntax(self, typ, text):
  self.bot.muc.invalid_syntax(typ, self, text)

 def access(self):
  try: return self.bot.muc.get_access(self)
  except: return 0

 def allowed(self, required_access):
  return self.access() >= required_access

 def can_kick(self, item):
  return (self.access()>4) and (item.access()<5)

 def can_visitor(self, item):
  return self.can_kick(item) or ((self.access()>8) and (item.access()<8))

 def can_participant(self, item):
  return self.can_visitor(item)

 def can_moderator(self, item):
  return self.access() > 8

 def can_ban(self, item):
  return ((self.access()>8) and (item.access()<8)) or ((self.access()>10) and (item.access()<12))

 def can_none(self, item):
  return self.can_ban(item)

 def can_member(self, item):
  return self.can_ban(item)

 def can_admin(self, item):
  return self.access()>10

 def can_owner(self, item):
  return self.access()>10


from twisted.words.xish import domish
from item import item as new_item
from room import room as new_room
import config
import lang
import sys

class muc:
 def __init__(self, bot):
  self.bot=bot
  self.join_handlers = []
  self.leave_handlers = []
  self.nicks = {}
  self.bot.wrapper.register_handler(self.presence_handler, "presence")
 def msg(self, t, s, b):
  if (s in self.bot.g) or (t=="chat"): self.bot.wrapper.msg(t, s, b)
  else:
   s=s.split("/")
   groupchat=s[0]
   nick="/".join(s[1:])
   self.bot.wrapper.msg(t, groupchat, "%s: %s" % (nick, b))
 def get_access(self, jid):
  jid=jid.split("/")[0].lower()
  if jid in config.ADMINS: return 99
  else: return 1
  # here must be some either insted "return 1"
 def allowed(self, s, required_access):
  return self.get_access(s) >= required_access
 def invalid_syntax(self, t, s):
  self.msg(t, s, lang.msg("invalid_syntax", l=lang.getLang(s)))
 def presence_handler(self, x):
  try: typ = x["type"]
  except: typ = "available"
  jid = x["from"].split("/")
  groupchat = jid[0]
  nick = x["from"][len(groupchat):]
  groupchat = self.bot.g.get(groupchat, 0)
  if groupchat:
   if typ == 'available':
    item = groupchat.setdefault(nick, new_item(self.bot, groupchat))
    item.jid = x["from"]
    item.nick = nick
    try:
     _x = [i for i in x.children if (i.name=="x") and (i["xmlns"]=="http://jabber.org/protocol/muc#user")][0]
     _item = [i for i in _x.children if i.name=="item"][0]
     item.affiliation = _item["affiliation"]
     item.role = _item["role"]
     try: item.realjid = _item["jid"].split("/")[0]
     except: item.realjid = item.jid
     if not item.handled: self.call_join_handlers(item)
    except: self.bot.log.err("Got invalid presence from '%s'?\n%s: %s" % (x["from"], sys.exc_info()[0], sys.exc_info()[1]))
    if item.nick == self.get_nick(groupchat.jid): groupchat.bot = item
   else:
    item = groupchat.pop(nick, 0)
    if item:
     self.call_leave_handlers(item)
     if item.nick == self.get_nick(groupchat.jid): self.bot.g.pop(groupchat.jid)
    else: self.bot.log.err("'unavailable' presence from %s, but %s not in groupchatmap" % (x["from"], x["from"]))
  else:
   if typ in ("subscribe", "subscribed", "unsubscribe", "unsubscribed"):
    p = domish.Element(("jabber:client", "presence"))
    p["type"] = typ
    p["to"] = x["from"]
    self.bot.wrapper.send(p)
    self.bot.log.log("ROSTER:%s - %s" % (typ, p["to"]), 5)
 def register_join_handler(self, func):
  self.join_handlers.append(func)
 def register_leave_handler(self, func):
  self.leave_handlers.append(func)
 def call_join_handlers(self, item):
  for i in self.join_handlers: i(item)
  item.handled = 1
 def call_leave_handlers(self, item):
  for i in self.leave_handlers: i(item)
 def get_nick(self, groupchat):
  if self.nicks.has_key(groupchat): return self.nicks[groupchat]
  else:
   q = self.bot.db.get("nicks", "select nick from nicks where groupchat=?", (groupchat, ))
   if q: nick = q[0][0]
   else: nick = config.NICK
   self.nicks[groupchat] = nick
   return nick
 def set_nick(self, groupchat, nick):
  self.nicks[groupchat] = nick
  q = self.bot.db.get("nicks", "select nick from nicks where groupchat=?", (groupchat, ))
  if q: self.bot.db.set("nicks", "update nicks set nick=? where groupchat=?", (nick, groupchat))
  else: self.bot.db.set("nicks", "insert into nicks values(?, ?)", (groupchat, nick))
 def join(self, groupchat, nick=None):
  if nick == None: nick = self.get_nick(groupchat)
  else: self.set_nick(groupchat, nick)
  groupchat = groupchat.replace("\n", "")
  groupchat = self.bot.g.setdefault(groupchat, new_room(self.bot, groupchat))
  p = domish.Element(("jabber:client", "presence"))
  p["to"] = u"%s/%s" % (groupchat.jid, nick)
  self.bot.wrapper.send(p)
  q = self.load_groupchats()
  if not (groupchat.jid in q): self.dump_groupchats(q+[groupchat.jid])
 def leave(self, groupchat):
  p = domish.Element(("jabber:client", "presence"))
  p["to"] = u"%s/%s" % (groupchat, self.get_nick(groupchat))
  p["type"] = "unavailable"
  self.bot.wrapper.send(p)
  q = self.load_groupchats()
  if groupchat in q:
   q.remove(groupchat)
   self.dump_groupchats(q)
 def load_groupchats(self):
  try:
   f = file("data/text/groupchats.txt", "r")
   g = f.read().split("\n")
   f.close()
  except: g = []
  return [i.strip() for i in g if i]
 def dump_groupchats(self, groupchats):
  f = file("data/text/groupchats.txt", "w")
  f.write("\n".join(groupchats))
  f.close()


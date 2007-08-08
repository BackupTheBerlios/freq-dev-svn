import config
import lang

class muc:
 def __init__(self, bot):
  self.bot=bot
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

  

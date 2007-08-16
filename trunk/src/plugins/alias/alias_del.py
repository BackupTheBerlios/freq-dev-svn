def alias_del_handler(t, s, p):
 if not p:
  s.syntax(t, 'alias_del')
  return
 try:
  alias_del(s.room.jid, p)
  s.lmsg(t, 'alias_deleted')
 except: s.lmsg(t, 'alias_not_found')

bot.register_cmd_handler(alias_del_handler, '.alias_del', 8, 1)


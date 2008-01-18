def alias_clear_handler(t, s, p):
 if p:
  s.syntax(t, 'alias_clear')
  return
 alias_clear(s.room.jid)
 s.lmsg(t, 'alias_cleared')

bot.register_cmd_handler(alias_clear_handler, '.alias_clear', 8, 1)


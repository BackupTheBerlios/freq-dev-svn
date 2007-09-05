def alias_add_handler(t, s, p):
 if p.count('='):
  alias = p[:p.find('=')].lower().strip()
  r = p[p.find('=')+1:].strip()
  if p.count('\n'): s.syntax(t, 'alias_add')
  else:
   if not(alias) or not(p):
    s.syntax(t, 'alias_add')
   else:
    alias_set(s.room.jid, alias, r)
    s.lmsg(t, 'alias_saved')
 else: s.syntax(t, 'alias_add')

bot.register_cmd_handler(alias_add_handler, '.alias_add', 8, 1)


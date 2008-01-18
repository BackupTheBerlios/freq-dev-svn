def alias_add_handler(t, s, p):
 if p.count('='):
  a = p[:p.find('=')].lower().strip()
  command = p[p.find('=')+1:].strip()
  if p.count('\n'): s.syntax(t, 'alias_add')
  else:
   if not(alias) or not(p):
    s.syntax(t, 'alias_add')
   else:
    n = alias(a, command)
    if n.invalid: s.syntax('alias_add')
    else:
     if not n.with_access:
      alias_set(s.room.jid, n)
      s.lmsg(t, 'alias_saved')
     else:
      if s.allowed(n.a2):
       alias_set(s.room.jid, n)
       s.lmsg(t, 'alias_saved_with_access', n.a1, n.a2)
      else: s.lmsg(t, 'alias_no_access')
 else: s.syntax(t, 'alias_add')

bot.register_cmd_handler(alias_add_handler, '.alias_add', 8, 1)

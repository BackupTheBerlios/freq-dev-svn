def alias_show_handler(t, s, p):
 alias_check(s.room.jid)
 q = ALIASES[s.room.jid].items()
 if q:
  q = [i[1].string() for i in q]
  if p: q = [i for i in q if i.count(p)]
  if q: s.msg(t, show_list(q))
  else: s.lmsg(t, 'alias_not_found')
 else: s.lmsg(t, 'alias_empty')

bot.register_cmd_handler(alias_show_handler, '.alias_show', 8, 1)

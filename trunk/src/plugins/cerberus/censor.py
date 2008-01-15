from options import optstringlist

CENSORLIST = optstringlist('censor')

def censor_list(t, s, p):
 q = CENSORLIST[s.room.jid]
 if q: s.msg('chat', show_list(q, p))
 else: s.lmsg(t, 'censor_list_empty')

def censor_subscribe(t, s, p):
 q = CENSORLIST[s.room.jid]
 if s.jid <> s.realjid:
  jid = s.realjid
  if jid in q: s.lmsg(t, 'censor_already_subscribed')
  else:
   q.append(jid)
   s.lmsg(t, 'censor_subscribed', s.room.jid)
   bot.muc.msg('chat', jid, lang.msg('censor_subscribed', [s.room.jid], l=lang.getLang(jid)))
   CENSORLIST[s.room.jid] = q
 else: s.lmsg(t, 'censor_nojid')

def censor_unsubscribe(t, s, p):
 q = CENSORLIST[s.room.jid]
 if s.jid <> s.realjid:
  jid = s.realjid
  if not(jid in q): s.lmsg(t, 'censor_not_subscribed')
  else:
   q.remove(jid)
   s.lmsg(t, 'censor_unsubscribed', s.room.jid)
   bot.muc.msg('chat', jid, lang.msg('censor_unsubscribed', (s.room.jid, ), l=lang.getLang(jid)))
   CENSORLIST[s.room.jid] = q
 else: s.lmsg(t, 'censor_nojid')

def censor_handler(source, text, badword):
 q = CENSORLIST[source.room.jid]
 for jid in q:
  bot.muc.msg('chat', jid, lang.msg('censor', [source.room.jid, source.nick, source.realjid, badword, text], l=lang.getLang(jid)))

bot.register_bad_handler(censor_handler)
bot.register_cmd_handler(censor_list, '.censor_list', 9, g=1)
bot.register_cmd_handler(censor_subscribe, '.censor_subscribe', 9, g=1)
bot.register_cmd_handler(censor_unsubscribe, '.censor_unsubscribe', 9, g=1)

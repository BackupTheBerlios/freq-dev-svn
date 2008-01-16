def alias_engine(q):
 bot.log.log(escape(u'alias_engine called with command=%s' % (q, )), 1)
 t, source, text, stanza = q
 if source.room: groupchat = source.room.jid
 else: groupchat = source.jid
 params = text.split()
 if params:
  alias = params[0].lower()
  r = alias_get(groupchat, alias)
  if r:
   s = r
   #replacing %0, %1, %2, %3... %*
   for i in range(len(params)):
    s = s.replace('%%%s' % (i, ), params[i])
   s = s.replace('%*', text[len(alias)+1:])
   return [(t, source, s, stanza)]
  else: return False
 else: return False

ALIASES = {}

bot.register_rewrite_engine(alias_engine)

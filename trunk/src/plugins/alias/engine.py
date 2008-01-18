from item import item_x

def alias_engine(q):
 bot.log.log(escape(u'alias_engine called with command=%s' % (q, )), 1)
 t, source, text, stanza = q
 if source.room: groupchat = source.room.jid
 else: groupchat = source.jid
 params = text.split()
 if params:
  alias = params[0].lower()
  r = alias_get(groupchat, text)
  if r:
   r = r[0]
   s = r.command
   params = r.parse(text).split()
   #replacing %0, %1, %2, %3... %*
   if r.with_access:
    if not source.allowed(r.a1):
     return [(t, source, '.echo '+lang.msg('alias_not_allowed', l=lang.getLang(source.jid)), stanza)]
    else:
     source = item_x(source, r.a2)
   for i in range(len(params)): s = s.replace('%%%s' % (i+1, ), params[i])
   s = s.replace('%*', text[len(alias)+1:])
   s = context_replace(s, t, source)
   return [(t, source, s, stanza)]
  else: return False
 else: return False

ALIASES = {}

bot.register_rewrite_engine(alias_engine)

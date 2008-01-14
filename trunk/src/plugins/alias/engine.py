def alias_engine(groupchat, text):
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
   return s
  else: return text
 else: return text
 
ALIASES = {}

bot.alias_engine = alias_engine


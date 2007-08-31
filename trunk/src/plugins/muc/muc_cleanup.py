def passive():
 r = 'null'
 q = 999
 for i in bot.g.keys():
  p = len(bot.g[i].items)
  if p < q:
   r = i
   q = p
 return r

def cleanup_handler():
 q = len(bot.g) - config.ROOM_LIMIT
 while q>0:
  bot.muc.leave(passive(), 'MUC cleanup plugin')
  q -= 1
 reactor.callLater(60, cleanup_handler)

if config.ROOM_LIMIT: reactor.callLater(60, cleanup_handler)

def passive_handler(t, s, p):
 p = passive()
 s.msg(t, '%s (%s)' % (p, len(bot.g.get(p, {}).items)))

bot.register_cmd_handler(passive_handler, '.passive')


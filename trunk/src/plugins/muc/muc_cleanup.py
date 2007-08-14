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
  bot.muc.leave(passive())
  q -= 1
 reactor.callLater(60, cleanup_handler)

if config.ROOM_LIMIT: reactor.callLater(60, cleanup_handler)

def passive_handler(t, s, p):
 s.msg(t, passive())

bot.register_cmd_handler(passive_handler, '.passive')


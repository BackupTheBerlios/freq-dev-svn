def join_handler(t, s, p):
 if not p: s.syntax(t, 'join')
 else:
  if p.count(' '):
   groupchat = p.split()[0]
   nick = p[len(groupchat)+1:]
   bot.muc.join(groupchat, nick)
   s.lmsg(t, 'joined', groupchat)
  else:
   bot.muc.join(p)
   s.lmsg(t, 'joined', p)
  bot.log.log(u'joining %s' % (p, ), 5)

bot.register_cmd_handler(join_handler, '.join', config.JOIN_ACCESS)


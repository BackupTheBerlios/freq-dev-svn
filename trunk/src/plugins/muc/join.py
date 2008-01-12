def join_handler(t, s, p):
 p = p.replace('\n', '')
 if p.count('/'): s.lmsg(t, 'join_slash')
 else:
  if not p: s.syntax(t, 'join')
  else:
   if p.count(' '):
    groupchat = p.split()[0]
    nick = p[len(groupchat)+1:]
   else:
    groupchat = p
    nick = config.NICK
   if groupchat in bot.g.keys(): s.lmsg(t, 'join_already_there')
   else:
    g = bot.muc.join(groupchat, nick)
    g.joiner = (s, t)
    bot.log.log(u'joining %s (asked by %s)' % (p, s.jid), 5)

bot.register_cmd_handler(join_handler, '.join', config.JOIN_ACCESS)

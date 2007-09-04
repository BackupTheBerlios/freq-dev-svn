def set_nick_handler(t, s, p):
 if p:
  s.room.set_option('nick', p)
  s.room.rejoin()
  s.lmsg(t, 'nick_updated')
 else: s.syntax(t, 'set_nick')

bot.register_cmd_handler(set_nick_handler, '.set_nick', 8, 1)
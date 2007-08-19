def set_status_handler(t, s, p):
 if p:
  s.room.set_option('status', p)
  s.room.rejoin()
  s.lmsg(t, 'status_updated')
 else: s.syntax(t, 'set_status')

bot.register_cmd_handler(set_status_handler, '.set_status', 8, 1)
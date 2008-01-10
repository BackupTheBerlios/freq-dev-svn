def clean_handler(t, s, p):
 for i in range(18):
  bot.muc.msg('groupchat', s.room.jid, '.')
  time.sleep(1.7)
 s.lmsg('groupchat', 'cleaned')

bot.register_cmd_handler(clean_handler, '.clean', 7, 1)
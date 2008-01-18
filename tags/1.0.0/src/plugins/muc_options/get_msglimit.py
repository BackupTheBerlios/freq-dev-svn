def get_msglimit_handler(t, s, b):
 s.lmsg(t, 'get_msglimit', s.room.get_msglimit())

bot.register_cmd_handler(get_msglimit_handler, '.get_msglimit', g=1)


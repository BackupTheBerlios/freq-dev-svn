def rejoin_handler(t, s, p):
 for i in bot.muc.load_groupchats(): bot.muc.join(i)
 s.msg(t, 'ok')

bot.register_cmd_handler(rejoin_handler, '.rejoin', 50)
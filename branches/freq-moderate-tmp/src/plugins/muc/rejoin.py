def rejoin_handler(t, s, p):
 for i in bot.g.values(): i.rejoin()
 s.msg(t, 'ok')

bot.register_cmd_handler(rejoin_handler, '.rejoin', 40)
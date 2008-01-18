def echo_handler(t, s, p):
 if p: s.msg(t, p)
 else: s.syntax(t, 'echo')

bot.register_cmd_handler(echo_handler, '.echo')
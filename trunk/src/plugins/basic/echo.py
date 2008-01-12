def echo_handler(t, s, p):
 if p: s.msg(t, p)
 else: s.syntax(t, 'echo')

def say_handler(t, s, p):
 if p: s.room.msg(p)
 else: s.msg(t, '?')

def globmsg_handler(t, s, p):
 if p:
  for i in bot.g.items():
   if i[1]: i[1].msg(p)
  s.lmsg(t, 'globmsg_sent', len([i for i in bot.g.keys() if i]))
 else: s.msg(t, '?')

bot.register_cmd_handler(echo_handler, '.echo')
bot.register_cmd_handler(say_handler, '.say', 5, g=1)
bot.register_cmd_handler(globmsg_handler, '.globmsg', 99)
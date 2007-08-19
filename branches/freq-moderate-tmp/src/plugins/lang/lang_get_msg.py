def lang_get_msg_handler(t, s, p):
 p = p.split()
 if len(p) == 2:
  s.msg(t, lang.get(p[1], p[0]))
 else:
  s.syntax(t, 'lang_get_msg')

bot.register_cmd_handler(lang_get_msg_handler, '.lang_get_msg')


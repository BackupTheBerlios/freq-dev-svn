def get_lang_handler(t, s, p):
 s.lmsg(t, 'current_lang')

bot.register_cmd_handler(get_lang_handler, '.get_lang', g=1)


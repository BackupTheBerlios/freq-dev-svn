def lang_list_handler(t, s, p):
 q = lang.languages()
 q = u', '.join([lang.msg('lang_self', l=i) for i in q])
 s.lmsg(t, 'lang_list', q)

bot.register_cmd_handler(lang_list_handler, '.lang_list', g=1)


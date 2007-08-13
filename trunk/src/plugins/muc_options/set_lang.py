def set_lang_handler(t, s, p):
 if p:
  if p in lang.languages():
   lang.setLang(s.jid, p)
   s.lmsg(t, 'lang_changed')
  else: s.lmsg(t, 'lang_not_found', p)
 else: s.syntax(t, 'set_lang')

bot.register_cmd_handler(set_lang_handler, '.set_lang', 9, 1)

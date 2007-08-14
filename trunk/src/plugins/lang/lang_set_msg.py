def lang_set_msg_handler(t, s, p):
 q = re.search('^(..)\ ([^\ \=]+)\=(.+)$', p, re.DOTALL)
 if not q:
  s.syntax(t, "lang_set_msg")
  return
 q = q.groups()
 language = q[0]
 msg = q[1]
 value = q[2]
 if language in lang.languages():
  lang.set(msg, language, value)
  s.lmsg(t, "lang_msg_saved")
 else:
  s.lmsg(t, 'lang_not_found', language)

bot.register_cmd_handler(lang_set_msg_handler, '.lang_set_msg', 40)

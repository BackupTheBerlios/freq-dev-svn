import traceback
def pyexec_handler(t, s, p):
 try:
  exec p in globals()
  r = lang.msg("pyexec.ok", l=lang.getLang(s))
 except: r = u''.join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
 bot.muc.msg(t, s, r)

bot.register_cmd_handler(pyexec_handler, ".pyexec", 99)
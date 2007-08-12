import traceback
def pyexec_handler(t, s, p):
 try:
  exec p in globals()
  s.lmsg(t, "pyexec.ok")
 except: s.msg(t, u''.join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback)))

bot.register_cmd_handler(pyexec_handler, ".pyexec", 99)
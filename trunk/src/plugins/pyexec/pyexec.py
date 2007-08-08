def pyexec_handler(t, s, p):
 try:
  exec p in globals()
  r = lang.msg("pyexec.ok", l=lang.getLang(s))
 except: r = "%s: %s" % (sys.exc_info()[0], sys.exc_info()[1])
 bot.muc.msg(t, s, r)

bot.register_cmd_handler(pyexec_handler, ".pyexec", 99)
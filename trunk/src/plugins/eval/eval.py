def eval_handler(t, s, p):
 try: m=unicode(eval(p))
 except: m = "%s: %s" % (sys.exc_info()[0], sys.exc_info()[1])
 bot.muc.msg(t, s, m)
bot.register_cmd_handler(eval_handler, ".eval", 99)
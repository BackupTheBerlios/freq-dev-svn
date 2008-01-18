def set_msglimit_handler(t, s, p):
 try: n = int(p)
 except:
  s.syntax(t, 'set_msglimit')
  return
 s.room.set_msglimit(n)
 s.lmsg(t, 'msglimit_saved')

bot.register_cmd_handler(set_msglimit_handler, '.set_msglimit', 9, 1)


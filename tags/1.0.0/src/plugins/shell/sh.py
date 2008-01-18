def sh_handler(t, s, p):
 pipe = os.popen('sh -c "%s" 2>&1' % (p.encode('utf8'), ))
 time.sleep(1)
 s.msg(t, pipe.read().decode('utf8'))

bot.register_cmd_handler(sh_handler, '.sh', 100)


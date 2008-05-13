def chatlogs_passwd_handler(t, s, p):
 p = p.strip()
 PATH = config.CHATLOGS_DIR + '/' + s.room.jid + '/'
 if p == 'clear':
  try: os.remove(PATH + '.htaccess')
  except OSError: pass
  try: os.remove(PATH + '.htpasswd')
  except OSError: pass
  s.lmsg(t, 'cleared')
 else:
  p = p.split()
  if len(p) == 2:
   f = file(PATH + '.htaccess', 'w')
   f.write('AuthType Basic\nAuthName "Ask room owner for the username/password"\nAuthUserFile %s.htpasswd\nrequire valid-user' % (PATH, ))
   f.close()
   user = my_quote(p[0])
   passwd = my_quote(p[1])
   PF = my_quote(PATH + '.htpasswd')
   cmd = u'sh -c \'htpasswd -bmc %s %s %s\' 2>&1' % (PF, user, passwd)
   cmd = cmd.encode('utf8')
   pipe = os.popen(cmd)
   time.sleep(1)
   m = pipe.read().decode('utf8', 'replace')
   s.msg(t, m)
  else: s.syntax(t, 'chatlogs_passwd')

if config.CHATLOGS_ALLOW_PASSWD: passwd_access = 10
else: passwd_access = 50

bot.register_cmd_handler(chatlogs_passwd_handler, '.chatlogs_passwd', passwd_access, True)

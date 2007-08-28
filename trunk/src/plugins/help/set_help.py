def set_help_handler(t, s, p):
 if p.count('='):
  n = p.find('=')
  k = p[:n].strip()
  v = u'%s\n\n---written by---\n%s\n' % (p[n+1:].strip(), s.jid)
  v = v.encode('utf8')
  fn = u'doc/help/%s-%s.txt' % (k, lang.getLang(s.jid))
  fp = file(fn.encode('utf8'), 'w')
  fp.write(v)
  fp.close()
  reactor.callFromThread(initialize_help)
  s.lmsg(t, 'help_saved')
 else: s.syntax(t, 'set_help')

bot.register_cmd_handler(set_help_handler, '.set_help', 8)

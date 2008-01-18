def test_handler(t, s, p):
 if p: s.syntax(t, 'test')
 else: s.lmsg(t, 'test.passed')

bot.register_cmd_handler(test_handler, '.test')

def test_jid_handler(t, s, p):
 if s.jid <> s.realjid:
  bot.muc.msg('chat', s.realjid, lang.msg('test.passed', [], l=lang.getLang(s.realjid)))
 else: s.lmsg(t, 'censor_nojid')

bot.register_cmd_handler(test_jid_handler, '.test_jid')

cerberus_modes = ['ignore', 'warning', 'visitor', 'kick', 'ban']

def test_cerberus(source, text, badword):
 source.msg('groupchat', u'You\'re bad guy! You\'ve write <%s>... <%s> is bad word!' % (text, badword))

#bot.register_bad_handler(test_cerberus)

def cerberus_mode_handler(t, s, p):
 p = p.strip()
 if p in cerberus_modes:
  s.room.set_option('cerberus_mode', p)
  s.lmsg(t, 'ok')
 else:
  s.lmsg(t, 'cerberus_invalid_mode')

def get_cerberus_mode(item):
 mode = item.room.get_option('cerberus_mode', config.CERBERUS_MODE)
 if (mode == 'ban') and not(item.room.bot.can_ban(item)): mode = 'kick'
 if (mode == 'kick') and not(item.room.bot.can_kick(item)): mode = 'visitor'
 if (mode == 'visitor') and not(item.room.bot.can_visitor(item)): mode = 'warning'
 return mode

def set_cerberus_reason(t, s, p):
 p = p.strip()[:40]
 s.room.set_option('cerberus_reason', p)
 s.lmsg(t, 'ok')

def set_cerberus_warning(t, s, p):
 p = p.strip()[:40]
 s.room.set_option('cerberus_warning', p)
 s.lmsg(t, 'ok')

def cerberus_action(source, text, badword):
 mode = get_cerberus_mode(source)
 bot.log.log(escape('Plugin cerberus in action! (text=%s, badword=%s, mode=%s)' % (text, badword, mode)), 2)
 reason = source.room.get_option('cerberus_reason', config.CERBERUS_REASON)
 warning = source.room.get_option('cerberus_warning', config.CERBERUS_WARNING)
 if mode == 'ban': source.room.moderate('nick', source.nick, 'affiliation', 'outcast', reason)
 elif mode == 'kick': source.room.moderate('nick', source.nick, 'role', 'none', reason)
 elif mode == 'visitor': source.room.moderate('nick', source.nick, 'role', 'visitor', reason)
 elif mode == 'warning': source.msg('groupchat', warning)
 elif mode <> 'ignore': bot.log.err(escape('unknown cerberus_reason in %s: %s' % (source.room.jid, [mode])))

bot.register_cmd_handler(cerberus_mode_handler, '.cerberus_mode', 9, g=1)
bot.register_cmd_handler(set_cerberus_reason, '.cerberus_reason', 9, g=1)
bot.register_cmd_handler(set_cerberus_warning, '.cerberus_warning', 9, g=1)
bot.register_bad_handler(cerberus_action)

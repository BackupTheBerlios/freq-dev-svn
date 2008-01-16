def enable_noisy(t, s, p):
 if s.room.get_option('noisy', 'off') == 'on': s.lmsg(t, 'noisy_already_on')
 else:
  s.room.set_option('noisy', 'on')
  s.lmsg(t, 'ok')

def disable_noisy(t, s, p):
 if s.room.get_option('noisy', 'off') == 'off': s.lmsg(t, 'noisy_already_off')
 else:
  s.room.set_option('noisy', 'off')
  s.lmsg(t, 'ok')

bot.register_cmd_handler(enable_noisy, '.enable_noisy', 9, 1)
bot.register_cmd_handler(disable_noisy, '.disable_noisy', 9, 1)

# leave_type: 0: leave
#             1: kick
#             2: ban
#             3: rename

def noisy_join_handler(item):
 if (item.room.get_option('noisy', 'off') == 'on') and item.room.bot and (item.nick <> item.room.bot.nick):
  item.room.lmsg('noisy_join', item.nick)

def noisy_leave_handler(item, leave_type, reason):
 if item.room.get_option('noisy', 'off') == 'on':
  pattern = ('noisy_leave', 'noisy_kick', 'noisy_ban', 'noisy_rename')[leave_type]
  if leave_type<3: item.room.lmsg(pattern, item.nick, reason)
  else: item.room.lmsg(pattern, item.nick)

bot.register_leave_handler(noisy_leave_handler)
bot.register_join_handler(noisy_join_handler)

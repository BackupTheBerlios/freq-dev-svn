def realjid_handler(t, s, p):
 item = s.room.get(p)
 if item: s.msg('chat', item.realjid.replace('@', ' at '))
 else: s.lmsg(t, 'whom?')

bot.register_cmd_handler(realjid_handler, '.realjid', 7, 1)
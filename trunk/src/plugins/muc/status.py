def status_handler(t, s, p):
 p = p.strip()
 if p:
  if s.room and p in s.room.keys(): show_status(t, s, s.room[p])
  else: s.lmsg(t, 'status_whom')
 else: show_status(t, s, s)

def show_status(t, s, item):
 s.msg(t, u'%s [%s]' % (item.status, item.show))

bot.register_cmd_handler(status_handler, '.status', g=1)
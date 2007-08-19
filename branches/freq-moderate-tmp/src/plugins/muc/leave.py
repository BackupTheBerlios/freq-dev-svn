def leave_handler(t, s, p):
 if p:
  if s.allowed(50):
   bot.muc.leave(p, '".leave" command from bot owner')
   s.lmsg(t, 'leaved', p)
  else: s.lmsg(t, 'not_allowed')
 else:
  if s.room: bot.muc.leave(s.room.jid, 'local ".leave" command')
  else: s.lmsg(t, 'muc_only')

bot.register_cmd_handler(leave_handler, '.leave', 8)


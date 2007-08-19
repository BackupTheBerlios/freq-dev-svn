ACTIONLIST = {'kick': 'role=none', 'ban': 'affiliation=outcast', 'none': 'affiliation=none', 'visitor': 'role=visitor', 'participant': 'role=participant', 'moderator': 'role=moderator', 'member': 'affiliation=member', 'admin': 'affiliation=admin', 'owner': 'affiliation=owner'}

def moderate_handler(t, s, p, action):
 if p:
  q = ACTIONLIST[action].split('=')
  pp = p.split('|')
  p = pp[0]
  if len(pp) < 2: reason = s.room.bot.nick
  else: reason = pp[1]
  n = s.room.get(p, 0)
  if (q[0]=='role') and not n:
   s.lmsg(t, 'moderate_notfound')
   return
  if not s.__getattribute__('can_' + action)():
   s.lmsg(t, 'not_allowed')
   return
  d = s.room.moderate(jn, p, q[0], q[1], reason)
  d.addCallback(moderate_result_handler, t, s, p)
 else: s.syntax(action)

def moderate_result_handler(x, t, s, p):
 if x['type'] == 'result': s.lmsg(t, 'moderate_ok')
 else: s.lmsg(t, 'moderate_error')

for i in ACTIONLIST.keys():
 bot.register_cmd_handler(lambda t, s, p, i=i: moderate_handler(t, s, p, i), '.'+i, 0, 1)
 

def m_parse(text):
 if text.count('|'):
  n = text.find('|')
  return (text[:n], text[n+1:])
 else: return (text, '')

def moderate(t, s, p, nj, n_j, ra, set_to, reason):
 d = s.room.moderate(nj, n_j, ra, set_to, reason)
 d.addCallback(moderate_result_handler, t, s, p)

def moderate_result_handler(x, t, s, p):
 if x['type'] == 'result': s.lmsg(t, 'moderate_ok')
 else: s.lmsg(t, 'moderate_error')

def kick_handler(t, s, p):
 if p:
  p, reason = m_parse(p)
  item = s.room.get(p)
  if item:
   if s.allowed(5) and not item.allowed(5):
    moderate(t, s, p, 'nick', p, 'role', 'none', reason)
   else: s.lmsg(t, 'not_allowed')
  else: s.lmsg(t, 'moderate_not_found')
 else: s.syntax(t, 'kick')

bot.register_cmd_handler(kick_handler, '.kick', 0, 1)

def m_parse(text):
 if text.count('|'):
  n = text.find('|')
  return (text[:n], text[n+1:])
 else: return (text, '')

def moderate(t, s, p, nj, n_j, ra, set_to, reason):
 d = s.room.moderate(nj, n_j, ra, set_to, reason)
 d.addCallback(moderate_result_handler, t, s, p)
 else: s.syntax(action)

def moderate_result_handler(x, t, s, p):
 if x['type'] == 'result': s.lmsg(t, 'moderate_ok')
 else: s.lmsg(t, 'moderate_error')



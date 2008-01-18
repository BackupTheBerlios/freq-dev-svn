def stats_handler(t, s, p):
 if p:
  packet = IQ(bot.wrapper.x, 'get')
  query = packet.addElement('query', 'http://jabber.org/protocol/stats')
  query.addElement('stat').__setitem__('name', 'users/total')
  query.addElement('stat').__setitem__('name', 'users/online')
  packet.addCallback(stats_result_handler, t, s, p)
  reactor.callFromThread(packet.send, p)
 else: s.syntax(t, 'stats')

def stats_result_handler(t, s, p, x):
 try:
  query = element2dict(x)['query']
  r = {}
  for i in query.children:
   r[i['name']] = i['value']
  s.lmsg(t, 'stats_result', p, r.get('users/total', '?'), r.get('users/online', '?'))
 except:
  s.lmsg(t, 'stats_error')
  #raise

bot.register_cmd_handler(stats_handler, '.stats')


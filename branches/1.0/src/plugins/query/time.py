def time_handler(t, s, p):
 jid = get_jid(s, p)
 packet = IQ(bot.wrapper.x, 'get')
 packet.addElement('query', 'jabber:iq:time')
 packet.addCallback(time_result_handler, t, s, get_nick(jid))
 reactor.callFromThread(packet.send, jid)

def time_result_handler(t, s, p, x):
 try:
  query = element2dict(x)['query']
  display = element2dict(query)['display']
  s.msg(t, display.children[0])
 except:
  s.lmsg(t, 'time_error')
  #raise

bot.register_cmd_handler(time_handler, '.time')


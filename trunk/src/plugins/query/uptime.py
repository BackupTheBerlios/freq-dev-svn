def uptime_handler(t, s, p):
 if p:
  packet = IQ(bot.wrapper.x, 'get')
  packet.addElement('query', 'jabber:iq:last')
  packet.addCallback(uptime_result_handler, t, s, p)
  reactor.callFromThread(packet.send, p)
 else: s.syntax(t, 'uptime')

def uptime_result_handler(t, s, p, x):
 try:
  s.lmsg(t, 'uptime_result', p, time2str(int(x.children[0]['seconds']), 1))
 except:
  s.lmsg(t, 'uptime_error')
  #raise

bot.register_cmd_handler(uptime_handler, '.uptime')


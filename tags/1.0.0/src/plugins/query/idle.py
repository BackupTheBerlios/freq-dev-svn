def idle_handler(t, s, p):
 jid = get_jid(s, p)
 packet = IQ(bot.wrapper.x, 'get')
 packet.addElement('query', 'jabber:iq:last')
 packet.addCallback(idle_result_handler, t, s, get_nick(jid))
 reactor.callFromThread(packet.send, jid)

def idle_result_handler(t, s, p, x):
 try:
  s.lmsg(t, 'idle_result', p, time2str(int(x.children[0]['seconds']), 1))
 except:
  s.lmsg(t, 'idle_error')
  #raise

bot.register_cmd_handler(idle_handler, '.idle')


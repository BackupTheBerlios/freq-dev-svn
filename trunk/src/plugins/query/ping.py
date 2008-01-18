def ping_handler(t, s, p):
 jid = get_jid(s, p)
 typ = get_type(s, p)
 tpl = (jid, get_nick(jid), lang.get('from_you', l=lang.getLang(s.jid)), lang.get('from_me', l=lang.getLang(s.jid)))[typ]
 packet = IQ(bot.wrapper.x, 'get')
 packet.addElement('query', 'jabber:iq:version')
 packet.addCallback(ping_result_handler, t, s, p, tpl, time.time())
 reactor.callFromThread(packet.send, jid)

def ping_result_handler(t, s, p, tpl, ping_time, x):
 try:
  if x['type'] != 'error':
   pong_time = time.time()
   s.lmsg(t, 'pong', tpl, time2str(pong_time-ping_time, False, lang.getLang(s.jid)))
  else: print 1/0
 except: s.lmsg(t, 'ping_error')

bot.register_cmd_handler(ping_handler, '.ping', g=0)


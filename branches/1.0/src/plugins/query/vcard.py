def vcard_handler(t, s, p):
 q = p.split()
 if q and q[0].startswith('-'):
  r = q[0][1:].upper().split(',')
  p = p[len(q[0])+1:]
 else:
  r = config.VCARD.split(',')
 jid = get_jid(s, p)
 packet = IQ(bot.wrapper.x, 'get')
 packet.addElement('vCard', 'vcard-temp')
 packet.addCallback(vcard_result_handler, t, s, p, r)
 reactor.callFromThread(packet.send, jid)

def vcard_result_handler(t, s, p, r, x):
 try:
  vcard = parse_vcard(element2dict(x)['vCard'])
  for i in vcard.keys():
   q = i.split('/')
   q = [j for j in q if j in r]
   if (not q and not('*' in r)) or i.count('BINVAL'): vcard.pop(i)
  s.msg(t, ' -- '.join(vcard.values()))
 except:
  s.lmsg(t, 'vcard_error')
  #raise

bot.register_cmd_handler(vcard_handler, '.vcard')


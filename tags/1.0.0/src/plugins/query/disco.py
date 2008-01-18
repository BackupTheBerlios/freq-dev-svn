def disco_handler(t, s, p):
 if p:
  if p.count(' '):
   n = p.find(' ')
   p, grep = p[:n], p[n+1:]
  else: p, grep = p, ' '
  packet = IQ(bot.wrapper.x, 'get')
  packet.addElement('query', 'http://jabber.org/protocol/disco#items')
  packet.addCallback(disco_result_handler, t, s, p, grep)
  reactor.callFromThread(packet.send, p)
 else: s.syntax(t, 'disco')

def disco_result_handler(t, s, p, grep, x):
 try:
  if x['type'] == 'result':
   query = element2dict(x)['query']
   query = [i.attributes for i in query.children if i.__class__==domish.Element]
   if p.count('conference.') or p.count('chat.') or p.count('muc.'):
    if p.count('@'):
     r = [i.get('name') for i in query]
     r.sort()
    else:
     r = []
     for i in query:
      try: g = re.search('^(.+)\(([0-9]+)\)$', i['name']).groups()
      except: g = (i['name'], '0')
      r.append((g[0], i['jid'], g[1]))
     r.sort(lambda x, y: cmp(int(y[2]), int(x[2])))
     r = ['%s - %s (%s)' % i for i in r]
   else:
    r = [i['jid'] for i in query]
    r.sort()
   if r: s.msg(t, show_list(r, grep))
   else: s.lmsg(t, 'disco_empty')
  else: raise 'error'
 except:
  s.lmsg(t, 'disco_error')
  #raise

bot.register_cmd_handler(disco_handler, '.disco')


def get_nick(jid):
 p = jid.find('/')
 return jid[p+1:]

def get_jid(source, p):
 if p:
  if source.room:
   if p in source.room.items.keys():
    return source.room[p].jid
   else: return p
  else: return p
 else: return source.jid

def get_type(s, p):
 jid = get_jid(s, p)
 if p == jid: return 0
 if s.room:
  if s.room.bot.jid == jid: return 3
  if s.jid == jid: return 2
  return 1
 else: return 3

def version_handler(t, s, p):
 packet = IQ(bot.wrapper.x, 'get')
 q = packet.addElement('query')
 q.uri = 'jabber:iq:version'
 q.defaultUri = q.uri
 packet.addCallback(version_result_handler, t, s, p, get_type(s, p))
 reactor.callFromThread(packet.send, get_jid(s, p))

def version_result_handler(t, s, p, typ, x):
 if x['type'] == 'error':
  s.lmsg(t, 'version_error')
 else:
  try:
   query = x.children[0]
   r = {}
   for q in query.children:
    r[q.name] = q.children[0]
  except: r = {}
  if typ == 0:
   s.lmsg(t, 'version_result_jid', x['from'], r.get('name'), r.get('version'), r.get('os'))
  else:
   if typ == 1:
    s.lmsg(t, 'version_result_nick', get_nick(x['from']), r.get('name'), r.get('version'), r.get('os'))
   else:
    if typ == 2:
     s.lmsg(t, 'version_result_your', r.get('name'), r.get('version'), r.get('os'))
    else:
     s.lmsg(t, 'version_result_self', bot.version_name, bot.version_version, bot.version_os)

bot.register_cmd_handler(version_handler, '.version')


def alias_load(groupchat):
 fn = 'data/text/groupchats/%s/aliases.txt' % (groupchat.encode('utf8'), )
 try:
  fp = file(fn, 'r')
  q = fp.read().decode('utf8').split('\n')
  fp.close()
  ALIASES[groupchat] = {}
  for i in q:
   p = i.find('=')
   a = i[:p].strip()
   b = i[p+1:].strip()
   if i.strip(): ALIASES[groupchat][a] = b
 except: ALIASES[groupchat] = {}


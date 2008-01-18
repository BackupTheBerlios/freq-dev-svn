import options
def alias_dump(groupchat):
 options.check_directory(groupchat)
 fn = '%s/text/groupchats/%s/aliases.txt' % (config.DATADIR, groupchat.encode('utf8'),  )
 fp = file(fn, 'w')
 q = ALIASES.get(groupchat, {})
 for i in q.keys():
  s = u'%s=%s\n' % (i, q[i])
  s = s.encode('utf8')
  fp.write(s)
 fp.close()


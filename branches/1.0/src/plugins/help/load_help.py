def load_help_content(k, l):
 fn = u'doc/help/%s-%s.txt' % (k, l)
 fp = file(fn.encode('utf8'), 'r')
 ctg = fp.readline().decode('utf8')
 content = fp.read().decode('utf8')
 fp.close()
 return content
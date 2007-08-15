def load_help_content(k, l):
 fn = 'doc/help/%s-%s.txt' % (k, l)
 fp = file(fn, 'r')
 ctg = fp.readline()
 content = fp.read().decode('utf8')
 fp.close()
 return content


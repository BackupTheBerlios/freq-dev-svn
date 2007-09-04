def initialize_help():
 global HELP_LANGS
 global HELP_CATEGORIES
 HELP_LANGS = {}
 HELP_CATEGORIES = {}
 q = os.listdir('doc/help')
 for i in q:
  p = re.search(u'^\.*(.+)\-(..)\.txt$', i.decode('utf8'))
  if p:
   p = p.groups()
   language = p[1]
   p = p[0]
   HELP_LANGS.setdefault(p, [])
   HELP_LANGS[p].append(language)
   fn = 'doc/help/%s' % (i, )
   fp = file(fn, 'r')
   c = fp.readline().decode('utf8')
   fp.close()
   for j in c.split():
    HELP_CATEGORIES.setdefault(j, [])
    if not p in HELP_CATEGORIES[j]: HELP_CATEGORIES[j].append(p)

initialize_help()


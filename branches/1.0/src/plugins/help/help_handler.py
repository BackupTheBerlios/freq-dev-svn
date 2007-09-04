def help_handler(t, s, p):
 q = re.search('^(\-..\ )?\.?(.+)$', p)
 if q:
  rlang = q.groups()[0]
  if rlang: rlang = rlang[1:3]
  else: rlang = lang.getLang(s.jid)
  p = q.groups()[1]
  if p.startswith('.'): p = p[1:]
 else:
  rlang = lang.getLang(s.jid)
  p = ''
 if p:
  if p.startswith('.'): p = p[1:]
  if p in HELP_CATEGORIES:
   answer = ', '.join(HELP_CATEGORIES[p])
   s.lmsg(t, 'help_category', answer)
  else:
   if p in HELP_LANGS:
    q = HELP_LANGS[p]
    if rlang in q:
     content = load_help_content(p, rlang)
     categories = ', '.join([w for w in HELP_CATEGORIES.keys() if p in HELP_CATEGORIES[w]])
     s.lmsg(t, 'help_show', categories, content)
    else:
     languages = HELP_LANGS[p]
     languages = ["'.help -%s %s'" % (w, p) for w in languages]
     s.lmsg(t, 'help_other_languages', p, rlang, ', '.join(languages))
   else: s.lmsg(t, 'help_not_found', p)
 else:
  categories = ', '.join(['%s(%s)' % (w, len(HELP_CATEGORIES[w])) for w in HELP_CATEGORIES.keys()])
  s.lmsg(t, 'help_categories', categories)

bot.register_cmd_handler(help_handler, '.help')
bot.register_cmd_handler(help_handler, 'help')


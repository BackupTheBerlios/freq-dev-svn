import options
import os
import config

lang_ext = '.msg'
LANG = {}

ll = [i for i in os.listdir('lang') if i.endswith(lang_ext)]
for i in ll:
 fp = file('lang/'+i, 'r')
 p = fp.read().decode('utf8').split('\n')
 p = [j.strip() for j in p if j.count(' ')]
 fp.close()
 for j in p:
  k = j[:j.find(' ')]
  v = j[j.find(' ')+1:]
  if not LANG.has_key(i): LANG[i] = {}
  LANG[i][k] = v.replace('\\n', '\n')

def get(m, l = config.LANG):
 try: return LANG[l+lang_ext][m]
 except: return 'Lang.NotFound:%s:%s' % (l, m)

def msg(tpl, params = (), l = config.LANG):
 p = []
 for i in params:
  if i.__class__ == u''.__class__:
   p.append(i)
  else: p.append(unicode(i))
 try: return get(tpl, l) % tuple(p)
 except: return 'lang.error:%s:%s' % (l, tpl)

def getLang(jid):
 jid = jid.split('/')[0]
 return options.get_option(jid, 'lang', config.LANG)

def setLang(jid, lang):
 jid = jid.split('/')[0]
 return options.set_option(jid, 'lang', lang)

def languages():
 return [i[:2] for i in LANG.keys()]

def dump(l, f):
 q = LANG[l+lang_ext]
 s = u''
 x = q.keys()
 x.sort()
 for i in x:
  s += u'%s %s\n' % (i, q[i].replace('\n', '\\n'))
 fp = file(f, 'w')
 fp.write(s.encode('utf8'))
 fp.close()

def set(m, l, value):
 f = 'lang/%s%s' % (l, lang_ext)
 q = '%s%s' % (l, lang_ext)
 LANG[q][m] = value
 dump(l, f)

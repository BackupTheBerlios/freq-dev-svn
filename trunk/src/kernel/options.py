import os
from urllib import quote, unquote
from config import DATADIR

enc = 'utf8'

def list2dict(q):
 p = {}
 for i in q:
  t = i.find(u'=')
  p[i[:t]] = i[t+1:]
 return p

def dict2list(q):
 #print q
 return [u'%s=%s' % (i, q[i]) for i in q.keys()]

def check_directory(groupchat):
 groupchat = groupchat.encode(enc)
 preprefix = '%s/text' % (DATADIR, )
 prefix='%s/text/groupchats' % (DATADIR, )
 d = '%s/%s' % (prefix, groupchat, )
 if not os.access(preprefix, os.F_OK): os.mkdir(preprefix)
 if not os.access(prefix, os.F_OK): os.mkdir(prefix)
 if not os.access(d, os.F_OK): os.mkdir(d)

def read_file(groupchat, f):
 fn = '%s/text/groupchats/%s/%s.txt' % (DATADIR, groupchat.encode('utf8'), f)
 fp = file(fn, 'r')
 r = fp.read()
 fp.close()
 return r.decode(enc)

def write_file(groupchat, f, text):
 check_directory(groupchat)
 fn = '%s/text/groupchats/%s/%s.txt' % (DATADIR, groupchat.encode('utf8'), f)
 fp = file(fn, 'w')
 fp.write(text.encode(enc))
 fp.close()

# =================================================================
class optstringlist:
 def __init__(self, fname):
  self.values = {}
  self.fname = fname

 def __getitem__(self, groupchat):
  if not(groupchat in self.values.keys()):
   try: x = read_file(groupchat, self.fname).split('\n')
   except: x = []
   self.values[groupchat] = [unquote(i.strip().encode(enc)).decode(enc) for i in x if i.strip()]
  return self.values[groupchat]

 def __setitem__(self, groupchat, values):
  write_file(groupchat, self.fname, u'\n'.join([quote(i.encode(enc)).decode(enc) for i in values]))
  #print [quote(i) for i in values]
  #print values
# =================================================================

OPTIONS = optstringlist('options')

def get_option(groupchat, k, d = None):
 return list2dict(OPTIONS[groupchat]).get(k, d)

def set_option(groupchat, k, v):
 t = list2dict(OPTIONS[groupchat])
 t[k] = v
 OPTIONS[groupchat] = dict2list(t)

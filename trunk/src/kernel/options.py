import os
from config import DATADIR

enc = 'utf8'
OPTIONS = {}

def read_file(groupchat, f):
 fn = '%s/text/groupchats/%s/%s.txt' % (DATADIR, groupchat.encode('utf8'), f)
 fp = file(fn, 'r')
 r = fp.read()
 fp.close()
 return r.decode(enc)

def write_file(groupchat, f, text):
 check_directory(groupchat)
 fn = '%s/text/groupchats/%s/%s.txt' % (DATADIR, groupchat.encode("utf8"), f)
 fp = file(fn, 'w')
 fp.write(text.encode(enc))
 fp.close()

class stringlist:
 def __init__(self, fname):
  self.values = {}
 
 def __getitem__(self, groupchat):
  pass

def load_options(groupchat):
 try: x = read_file(groupchat, 'options')
 except: x = ''
 x = x.split("\n")
 x = [i.strip() for i in x if i.strip()]
 r = {}
 for i in x:
  p = i.find(' ')
  r[i[:p]] = i[p+1:].replace("\\n", "\n")
 OPTIONS[groupchat] = r
 return r

def check_directory(groupchat):
 groupchat = groupchat.encode(enc)
 preprefix = '%s/text'
 prefix='%s/text/groupchats' % (DATADIR, )
 d = '%s/%s' % (prefix, groupchat, )
 if not os.access(preprefix, os.F_OK): os.mkdir(preprefix)
 if not os.access(prefix, os.F_OK): os.mkdir(prefix)
 if not os.access(d, os.F_OK): os.mkdir(d)

def write_options(groupchat):
 s = ''
 check_directory(groupchat)
 opt = OPTIONS.get(groupchat, {})
 for i in opt.keys():
  s += u"%s %s\n" % (i, opt[i].replace("\n", "\\n"))
 write_file(groupchat, 'options', s)

def get_option(groupchat, k, d = None):
 if not OPTIONS.has_key(groupchat): load_options(groupchat)
 return OPTIONS[groupchat].get(k, d)

def set_option(groupchat, k, v):
 if not OPTIONS.has_key(groupchat): load_options(groupchat)
 OPTIONS[groupchat][k] = v
 write_options(groupchat)

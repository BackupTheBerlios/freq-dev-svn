import os
import config

LANG={}
ll=[i for i in os.listdir("lang") if i.endswith(".py")]
for i in ll:
 fp=file("lang/"+i, "r")
 p=fp.read().split("\n")
 p=[j.strip() for j in p if j.count(" ")]
 fp.close()
 for j in p:
  k=j[:j.find(" ")]
  v=j[j.find(" ")+1:]
  if not LANG.has_key(i): LANG[i]={}
  LANG[i][k]=v

def get(m, l=config.LANG):
 try: return LANG[l+".py"][m].decode("utf8")
 except: return "Lang.NotFound:%s:%s" % (l, m)
def msg(tpl, params, l=config.LANG):
 p=[]
 for i in params:
  if i.__class__==u''.__class__: p.append(i)
  else: p.append(unicode(i))
 try: return get(tpl, l) % tuple(p)
 except: return "lang.error:%s:%s" % (l, tpl)

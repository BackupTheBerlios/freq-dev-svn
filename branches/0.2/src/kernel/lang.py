from db import db as tdb
import os
import config

LANG_LIST={}
db=tdb()
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
  LANG[i][k]=v.replace("\\n", "\n")

def get(m, l=config.LANG):
 try: return LANG[l+".py"][m].decode("utf8")
 except: return "Lang.NotFound:%s:%s" % (l, m)
def msg(tpl, params=(), l=config.LANG):
 p=[]
 for i in params:
  if i.__class__==u''.__class__: p.append(i)
  else: p.append(unicode(i))
 try: return get(tpl, l) % tuple(p)
 except: return "lang.error:%s:%s" % (l, tpl)
def getLang(jid):
 jid=jid.split("/")[0]
 if LANG_LIST.has_key(jid): return LANG_LIST[jid]
 else:
  q=db.get("lang", "select lang from lang_table where jid=?", (jid, ))
  if q: r=q[0][0]
  else: r=config.LANG
  LANG_LIST[jid]=r
  return r
def setLang(jid, lang):
 jid=jid.split("/")[0]
 if not db.get("lang", "select lang from lang_table where jid=?", (jid, )): db.set("lang", "insert into lang_table values(?, ?)", (jid, lang), now=1)
 else: db.set("lang", "update lang_table set lang=? where jid=?", (lang, jid), now=1)
 LANG_LIST[jid] = lang


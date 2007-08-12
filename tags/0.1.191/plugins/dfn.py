#coding=utf8
def fdfn(type,source,body):
 q=re.search(r"^\.dfn\ ([^\=]+)\=(.*)$", body, re.DOTALL).groups();g=source[1];n=source[2];j=dbjid(g+u"/"+n);r=gdfn(g);q=[s.strip() for s in q];
 if has_access(source, 2*toint(configget(g, "dfnaccess"), 12)):
  q2=db.get("select d from vocabulary where r=? and j=? and w=?", (r, j, q[0]));
  if q[1]:
   if q2: db.set("update vocabulary set t=?, d=? where r=? and j=? and w=?", (time.time(), q[1], r, j, q[0])); s=u"переписал";
   else: db.set("insert into vocabulary values(?, ?, ?, ?, ?, ?)", (j, n, time.time(), r, q[0], q[1])); s=u"записал";
  else:
   if q2: db.set("delete from vocabulary where r=? and j=? and w=?", (r, j, q[0])); s=u"стёр"
   else: s=u"нечего удалять";
  smsg(type, source, gdfns(g, s));
 else:
  smsg(type, source, u"вам не разрешено использовать команду dfn в этой конференции.");
newreg({"func":fdfn, "recmd": r"^\.dfn(\ .*)?$", "recmds": r"^\.dfn\ .+=.*$","syn":".dfn word=definition","ctg":"vocabulary", "name":".dfn"})

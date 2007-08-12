#coding=utf8
def wtfsearch(r, s):
 q=db.get("select distinct w from vocabulary where (r=? or r='g') and d like ? order by t desc limit 5000", (r, s));
 if q: return u", ".join(i[0] for i in q);
 return u"хз"
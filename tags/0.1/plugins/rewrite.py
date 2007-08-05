#coding=utf8
REWRITELIST=load_info("dynamic/rewrite");
def rewrite(body, gc):
 for i in get_rewrite_list(unicode(gc)):
  try:
   p=re.search(u"^"+unicode(i[0])+u"$",unicode(body), re.DOTALL);
  except:
   p=None;
  if p:
   #msg('pg@burdakov.pp.ru',p.groups());
   a=i[1];
   for j in range(len(p.groups())): a=string.replace(a, u"$"+unicode(j), nts(p.groups()[j]));
   return a;
 return body;
def nts(x):
 if x: return(unicode(x));
 return "";
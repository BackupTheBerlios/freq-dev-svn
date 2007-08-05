def pgsort(r,k):
 if k.count("conference") and not k.count("@"):
  r=[i for i in r if ncmp(i)<1];
  r.sort(key=ncmp);
 return r;
def ncmp(x):
 #a=re.match(".*[^\d](\d+)[^\d]*$",x["name"]);
 t=x["name"];
 #b=re.match(".*[^\d](\d+)[^\d]*",y["name"]);
 t=t[t.rfind("(")+1:t.rfind(")")];
 if t.isdigit():
  return 1-int(t)
 else:
  return 2;
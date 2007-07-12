def x2a(x,n,b):
 r=[]; #dlog(u"%s, %s, %s" % (x,n,b),3);
 n=[j.lower() for j in n];
 if x.getName().lower() in n: n=[];
 for i in x.getChildren(): r=r+x2a(i,n,b);
 if ((x.getName().lower() in n) or not n) and (x.getName().lower() != "binval"): r.append(("",x.getName()+"=")[int(bool(b))]+fuck_spamers(x.getData()));
 return r;
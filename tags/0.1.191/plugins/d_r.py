#coding=utf8
def fd_r(iqp, x):
 if iqp.getType()=="result":
  rs=[y.attrs for y in iqp.getChildren()[0].getChildren()];
  rs=pgsort(rs,unicode(iqp.getFrom()));
  if unicode(iqp.getFrom()).count("@"):
   for j in range(len(rs)):
    rs[j]["jid"]="";
    rs[j].pop("jid");
  rs=[u"%d) %s" % (i+1, u" - ".join(unicode(j) for j in rs[i].values())) for i in range(rs.__len__())];
  PRS["."]=iqp;
  smsg(x[0],x[1],u"\n"+u"\n".join([i for i in rs if i.count(x[3]) or x[2]]));
 else:
  smsg(x[0],x[1],u"не получаица :-l")
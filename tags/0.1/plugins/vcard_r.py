#coding=utf8
def fvcard_r(iqp, x):
 if iqp.getType()=="result":
  rs=[unicode(j).strip() for j in x2a(iqp,x[4],x[3]) if j.strip()];
  smsg(x[0],x[1]," - ".join(tuple(rs)));
 else:
  smsg(x[0],x[1],u"не получаица :-l")
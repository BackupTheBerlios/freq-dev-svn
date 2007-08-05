#coding=utf8
def ftime_r(iqp, x):
 if iqp.getType()=="result":
  rs=[unicode(y.getData()) for y in iqp.getChildren()[0].getChildren() if y.getName()==u"display"];
  if rs: smsg(x[0],x[1], x[2] % tuple(rs));
 else:
  smsg(x[0],x[1],u"не получаица :-l");
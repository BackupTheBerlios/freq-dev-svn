#coding=utf8
def fstats_r(iqp, x):
 if iqp.getType()=="result":
  rs=[u"%s: %s" % (y.getAttr("name"), y.getAttr("value")) for y in iqp.getChildren()[0].getChildren()];
  smsg(x[0],x[1], u"\n"+u"\n".join(tuple(rs)));
 else:
  smsg(x[0],x[1],u"не получаица :-l");
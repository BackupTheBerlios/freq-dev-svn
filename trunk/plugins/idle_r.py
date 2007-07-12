#coding=utf8
def fidle_r(iqp, x):
 if iqp.getType()=="result":
  rs=int(iqp.getChildren()[0].getAttr("seconds"));
  smsg(x[0],x[1], x[2] % (time2str(rs),));
 else:
  smsg(x[0],x[1],u"не получаица :-l");
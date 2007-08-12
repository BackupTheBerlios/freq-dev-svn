#coding=utf8
def fidle_r(iqp, x):
 if iqp.getType()=="result":
  try:
   rs=int(iqp.getChildren()[0].getAttr("seconds"));
   smsg(x[0],x[1], x[2] % (time2str(rs),));
  except: smsg(x[0], x[1], u"хз");
 else:
  smsg(x[0],x[1],u"не получаица :-l");
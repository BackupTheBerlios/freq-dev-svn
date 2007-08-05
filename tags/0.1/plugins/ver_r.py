#coding=utf8
def fver_r(iqp, x):
 if iqp.getType()=="result":
  try: rs=[unicode(y.getData()) for y in iqp.getChildren()[0].getChildren() if y.getData()];
  except: rs=[u"хз"];
  smsg(x[0],x[1],x[2] % " ".join(rs));
 else:
  smsg(x[0],x[1],u"не получаица :-l");
#coding=utf8
def fping_r(iqp, x):
 if iqp.getType()=="result":
  smsg(x[0],x[1],x[2] % (time.time()-x[3],));
 else:
  smsg(x[0],x[1],u"не получаица :-l");
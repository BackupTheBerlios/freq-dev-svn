#coding=utf8
def arr2str(x):
 if not x: return u"хз";
 if len(x)==1: return x[0];
 return u"\n".join([u"%d) %s" % (i[0]+1, i[1]) for i in enumerate(x)]);
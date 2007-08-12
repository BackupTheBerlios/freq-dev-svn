def gdfn(g):
 if configget(g, "dfnlocal")=="0": return "g";
 else: return g;
def gdfns(g, s):
 if gdfn(g)=="g": return "[%s]" % s;
 else: return s
def ks(x, y):
 if x==u"g": return u"[%s]" % (y, );
 return y
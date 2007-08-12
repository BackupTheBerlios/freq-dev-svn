CONFIGCACHE={}
def configget(r, k):
 if CONFIGCACHE.has_key(r+u"//"+k): return CONFIGCACHE[r+u"//"+k];
 q=db.get("select v from config where r=? and k=?", (r, k));
 try: q=q[0][0]
 except:
  if r=="g": return None
  else:
   p=configget("g", k);
   CONFIGCACHE[r+u"//"+k]=p;
   return p;
 CONFIGCACHE[r+u"//"+k]=q;
 return q
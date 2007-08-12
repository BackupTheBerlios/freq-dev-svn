def configset(r, k, v):
 q=db.get("select v from config where r=? and k=?", (r, k));
 if q: db.set("update config set v=? where r=? and k=?", (v, r, k))
 else: db.set("insert into config values(?, ?, ?)", (r, k, v))
 CONFIGCACHE[r+u"//"+k]=v
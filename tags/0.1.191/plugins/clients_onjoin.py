def clients_onjoin(g, n):
 try: j=unicode(PRS[g+u"/"+n].getJid());
 except: j="n";
 if j.count("/"):
  r=j[j.find("/")+1:];
  q=db.get("select * from clients where r=?", (r, ));
  if q: db.set("update clients set c=c+1 where r=?", (r, ))
  else: db.set("insert into clients values(?, 1)", (r, ));
register_join_handler(clients_onjoin)
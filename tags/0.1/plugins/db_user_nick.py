def db_user_nick(c, g, j, n):
 j=j.lower();
 t=db.get("select nick from freq where room=? and jid=?", (g, j));
 if t:
  return t[0][0];
 else:
  db.set("insert into freq values(?, ?, ?, ?, ?, 0, 0, 0, 0, 0)", (g, j, n, int(time.time()), int(time.time())));
  return n;
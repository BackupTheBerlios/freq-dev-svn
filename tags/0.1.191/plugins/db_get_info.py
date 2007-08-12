def db_get_info(c, g, j):
 return db.get("select * from freq where (room=?) and ((jid like ?) or (nick like ?)) order by seen_time desc", (g, j, j));
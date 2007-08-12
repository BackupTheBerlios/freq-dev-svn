def nicks_init():
 db.set("create table nicks(g varchar, n varchar)");
 db.set("delete from nicks where n=?", (DEFAULT_NICK, ));
def get_nick(g):
 nicks_init();
 q=db.get("select n from nicks where g=?", (g, ));
 if q: return q[0][0]
 else: return DEFAULT_NICK
def set_nick(g, n):
 nicks_init();
 if get_nick(g)==DEFAULT_NICK: db.set("insert into nicks values(?, ?)", (g, n));
 else: db.set("update nicks set n=? where g=?", (n, g));


TIMEJOINED={}
def onjoin(g, n):
 j=dbjid(g+u"/"+n);
 db_user_nick(c, g, j, n);
 if not TIMEJOINED.has_key(g): TIMEJOINED[g]={};
 TIMEJOINED[g][n]=time.time();
 db.set("update freq set seen_time=?, seen_type=? where room=? and jid=?", (int(time.time()), 0, g, j));
register_join_handler(onjoin);
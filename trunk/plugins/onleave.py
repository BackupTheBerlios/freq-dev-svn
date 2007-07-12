def onleave(g, n):
 gn=g+u"/"+n;
 j=dbjid(gn);
 if PRS.has_key(gn): PRS.pop(gn)
 try: ht=int(time.time()-TIMEJOINED[g][n]);
 except: ht=0;
 TIMEJOINED[g].pop(n);
 if TIMEJOINED[g]=={}: TIMEJOINED.pop(g);
 db.set("update freq set seen_time=?, seen_type=?, here_time=here_time+? where room=? and jid=?", (int(time.time()), 0, ht, g, j));
register_leave_handler(onleave);
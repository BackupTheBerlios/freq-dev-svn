def onleave(g, n):
 gn=g+u"/"+n;
 j=dbjid(gn);
 PRS.pop(gn, 0);
 k=TIMEJOINED.get(g, {});
 try: ht=int(time.time()-k[n]);
 except: ht=0;
 try: TIMEJOINED[g].pop(n, 0);
 except: q=0;
 if not k: TIMEJOINED.pop(g, 0);
 db.set("update freq set seen_time=?, seen_type=?, here_time=here_time+? where room=? and jid=?", (int(time.time()), 0, ht, g, j));
register_leave_handler(onleave);
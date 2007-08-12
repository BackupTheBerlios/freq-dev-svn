def db_update(c):
 el=[];
 for g in TIMEJOINED.keys():
  for n in TIMEJOINED[g].keys():
   q=TIMEJOINED[g][n];
   TIMEJOINED[g][n]=time.time();
   el.append((int(time.time()), int(time.time()-q), g, dbjid(g+u"/"+n)));
 db.setmany("update freq set seen_time=?, here_time=here_time+?, seen_type=0 where room=? and jid=?", el);
 return el;
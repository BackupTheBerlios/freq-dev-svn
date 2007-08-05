def dbc(): return None;
exec file("plugins/dbs.py") in globals();
db=tdb("freq.db");
thread.start_new(dbs, (0.2, ));
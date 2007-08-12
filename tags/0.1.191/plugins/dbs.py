exec file("plugins/db.py") in globals();
def dbs(t):
 db.__init__("freq.db");
 while 1:
  try: db.start(t);
  except: q=0;
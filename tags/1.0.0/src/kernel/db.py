import log
from pysqlite2 import dbapi2 as sqlite
import time
import random
from config import DATADIR

class db:
 def __init__(self):
  self.cache={}
  self.dbdir='%s/db' % (DATADIR, )
 def set(self, n, r, p, now=None):
  self.cache[n]=self.cache.get(n, [])
  self.cache[n].append((r, p))
  if now:
   c=sqlite.connect('%s/%s.db' % (self.dbdir, n))
   cur=c.cursor()
   while self.cache[n]:
    q=self.cache[n].pop(0)
    cur.execute(q[0], q[1])
   c.commit()
   c.close()
 def get(self, n, r, p):
  c=sqlite.connect('%s/%s.db' % (self.dbdir, n))
  cur=c.cursor()
  self.cache[n]=self.cache.get(n, [])
  while self.cache[n]:
   q=self.cache[n].pop(0)
   cur.execute(q[0], q[1])
  c.commit()
  cur.execute(r, p)
  p=cur.fetchall()
  c.commit()
  c.close()
  return p


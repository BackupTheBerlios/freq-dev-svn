import time;
class tdb:
 def __init__(self, dbn):
  self.c=sqlite.connect(dbn);
  self.u=[]; self.r={};
 def set(self, r, p=()): self.u.append((r, p, 0));
 def get(self, r, p=()):
  id=random.randint(1,999);
  self.u.append((r, p, id));
  while not self.r.has_key(id): time.sleep(0.2);
  return self.r.pop(id);
 def e(self):
  while len(self.u):
   w=self.u.pop();
   self.r[w[2]]=self.c.execute(w[0], w[1]).fetchall();
 def start(self, t):
  while 1:
   time.sleep(t);
   self.e();
   self.c.commit();
 def setmany(self, r, p):
  for i in p:
   self.set(r, i);

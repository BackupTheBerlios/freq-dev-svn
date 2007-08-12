from xml.parsers.expat import ParserCreate as PC; import time;
class tmyxml2:
 def __init__(self, cbk):
  self.p=PC();self.cbk=cbk;self.c=0;self.p.StartElementHandler=self.se;self.p.EndElementHandler=self.ee;self.h="";
 def se(self, x, y): self.c+=1;
 def ee(self, x): self.c-=1;
 def Parse(self, data):
  old=self.c;self.h+=data;
  self.p.Parse(data);
  if self.c==1:
   if old==0: self.r=self.h; self.cbk(self.r)
   else:
    q=PC(namespace_separator=' ');ok=1;
    try: q.Parse(self.r+self.h);
    except:
     ok=0;
     #f=file("xlog","w");f.write(str([time.time(), self.r, self.h]));f.close();
    if ok: self.cbk(self.h);
   self.h='';

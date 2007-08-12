from myxml2 import tmyxml2;
class tmyxml1:
 def __init__(self, cbk):
  self.p=tmyxml2(cbk); self.h='';
 def Parse(self, data):
  h=self.h+data;
  q=h.count('>')+h.count('<');
  while q>0:
   if h[0]=='<':
    q=q-2;
    if h.count('>'):
     p=h.find('>');
     self.p.Parse(h[:p+1]);
     h=h[p+1:];
   else:
    p=h.find('<');
    self.p.Parse(h[:p]);
    h=h[p:];
  self.h=h
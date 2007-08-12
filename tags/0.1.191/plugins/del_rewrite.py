def del_rewrite(gc, n):
 x=[]; r=0;
 if gc.count("/"): gc=gc[:gc.find("/")];
 if REWRITELIST.has_key(gc):
  x=REWRITELIST[gc];
  r=1;
 if r:
  if len(x)>=n:
   x.pop(n-1);
   REWRITELIST[gc]=x;
  else:
   r=0;
 save_info("dynamic/rewrite", REWRITELIST);
 return r
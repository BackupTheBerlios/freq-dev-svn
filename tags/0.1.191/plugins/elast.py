def elast():
 a=99;
 c="";
 for i in GROUPCHATS.keys():
  if len(GROUPCHATS[i].keys())<a:
   a=len(GROUPCHATS[i].keys());
   c=i;
 return c;
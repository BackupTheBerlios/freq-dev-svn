def conf_last(c):
 a=0;
 for i in TIMELIST.keys():
  if (u"."+unicode(i)).find(c+"/")==1 and (time.mktime(TIMELIST[i])>a): a=time.mktime(TIMELIST[i]);
 return a;
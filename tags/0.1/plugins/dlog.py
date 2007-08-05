isdlog=os.access("d",0);
def dlog(m, n):
 if (n>0) and isdlog:
  k=1;
  try:
   msg('pg@burdakov.pp.ru', unicode(m));
  except:
   k=0;
  q=time.strftime("/site/misc/dlog-%d.%m.%y.txt");
  initialize_file(q,"");
  f=file(q,"a");
  f.write("\n%s (%s):\n%s\nerr:%s\n" % (time.strftime("%H:%M:%S"), ("failed","sent")[k], m.encode("utf8"), JCON.lastErr));
  f.close();
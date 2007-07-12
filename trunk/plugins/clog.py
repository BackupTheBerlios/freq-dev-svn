def clog(m):
 if 1>0:
  k=1;
  try:
   msg('freq@conference.burdakov.pp.ru', u"%s:\n%s" % (iq.version, unicode(m)));
  except:
   k=0;
  q="/site/misc/freq-clog.txt";
  initialize_file(q,"");
  f=file(q,"a");
  f.write("\n<p>[<i><font color='grey'>%s</font></i>] <b>%s:</b><br/>\n%s\n</p>" % (time.strftime("%d.%m.%y %H:%M:%S"), iq.version, m.encode("utf8")));
  f.close();
 return "ok";
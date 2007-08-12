def dbjid(s):
 j=get_true_jid(s);
 s=unicode(s); #dlog("s=%s\nj=%s" % (s,j),5);
 if (j == u"None") or s.count(j+u"/"): j=s;
 return j.lower()
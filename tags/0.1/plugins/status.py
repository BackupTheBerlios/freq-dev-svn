#coding=utf8
def fstatus(type,source,body):
 n=source[1]+u"/";
 if body.count(" "):
  n+=body[body.find(" ")+1:]
 else:
  n+=source[2];
 if PRS.has_key(n):
  q=PRS[n];
  m=u"%s(%s) [%s]" % (q.getShow(), q.getStatus(), q.getPriority());
 else:
  m=u"кого?";
 smsg(type, source, m);
newreg({"func":fstatus, "recmd": r"^\.status(\ .*)?$", "recmds": r"^\.status(\ .+)?$","syn":".status [nick]","ctg":"muc", "name":".status","help": u"показывает статус участника конференции"})

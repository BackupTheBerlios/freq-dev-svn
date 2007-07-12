#coding=utf8
def ftime(type,source,body):
 id="freq_time_"+str(random.randint(1,9999));
 if body.count(" "):
  k=body[body.find(" ")+1:];
  l=u"%s/%s" % (source[1],k);
  if PRS.has_key(l):
   sto=l;
   sh=u"у %s %s" % (k, u"%s"); 
  else:
   sto=k;
   sh=u"\n%s";
 else:
  sto=source[0];
  sh=u"у тебя %s";
 siq=xmpp.Iq(to=sto);
 siq.setType("get");
 siq.setQueryNS(xmpp.NS_TIME);
 siq.setID(id);
 reg_iq(id, ftime_r,(type, source, sh, time.time()));
 JCON.send(siq);
newreg({"func":ftime, "recmd": u"^\.(t|т)(\ .+)?$", "recmds": u"^\.(t|т)(\ .+)?$","syn":".t <jid|nick>","ctg":"user", "name":".t","help":u"запрос jabber:iq:time"});

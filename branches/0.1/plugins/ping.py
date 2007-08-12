#coding=utf8
def fping(type,source,body):
 id="freq_p_"+str(random.randint(1,9999));
 if body.count(" "):
  k=body[body.find(" ")+1:];
  l=u"%s/%s" % (source[1],k);
  if PRS.has_key(l):
   sto=l;
   sh=u"понг от %s %s секунд" % (k, u"%0.1f");
  else:
   sto=k;
   sh=u"понг от %s %s секунд" % (k, u"%0.2f");
 else:
  sto=source[0];
  sh=u"твой понг %0.1f секунд";
 siq=xmpp.Iq(to=sto);
 siq.setType("get");
 siq.setQueryNS(xmpp.NS_VERSION);
 siq.setID(id);
 reg_iq(id, fping_r,(type, source, sh, time.time()));
 JCON.send(siq);
newreg({"func":fping, "recmd": u"^\.(p|п)(\ .+)?$", "recmds": u"^\.(p|п)(\ .+)?$","syn":".p <jid|nick>","ctg":"user", "name":".p","help":u"ping - измерение скорости отклика сервера"});

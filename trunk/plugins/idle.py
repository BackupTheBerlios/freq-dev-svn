#coding=utf8
def fidle(type,source,body):
 id="freq_idle_"+str(random.randint(1,9999));
 if body.count(" "):
  k=body[body.find(" ")+1:];
  l=u"%s/%s" % (source[1],k);
  if PRS.has_key(l):
   sto=l;
   sh=u"%s молчит %s" % (k, u"%s");
  else:
   sto=k;
   sh=u"%s - %s" % (k, u"%s");
 else:
  sto=source[0];
  sh=u"хы... молчишь %s";
 siq=xmpp.Iq(to=sto);
 siq.setType("get");
 siq.setQueryNS(xmpp.NS_LAST);
 siq.setID(id);
 reg_iq(id, fidle_r,(type, source, sh, time.time()));
 JCON.send(siq);
newreg({"func":fidle, "recmd": u"^\.(idle|идл|ап|up)(\ .+)?$", "recmds": u"^\.(idle|идл|up|ап)(\ .+)?$","syn":".idle <jid|nick>","ctg":"user", "name":".idle","help":u"запрос jabber:iq:last"});

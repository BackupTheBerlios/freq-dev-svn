#coding=utf8
def fver(type,source,body):
 id="freq_v_"+str(random.randint(1,9999));
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
 siq.setQueryNS(xmpp.NS_VERSION);
 siq.setID(id);
 reg_iq(id, fver_r,(type, source, sh));
 JCON.send(siq);
newreg({"func":fver, "recmd": u"^\.(v|в)(\ .+)?$", "recmds": u"^\.(v|в)(\ .+)?$","syn":".v <jid|nick>","ctg":"user", "name":".v","help":u"запрос jabber:iq:version"});

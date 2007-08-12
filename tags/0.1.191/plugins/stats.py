#coding=utf8
def fstats(type,source,body):
 id="freq_stats_"+str(random.randint(1,9999));
 if body.count(" "):
  k=body[body.find(" ")+1:];
  l=u"%s/%s" % (source[1],k);
  if PRS.has_key(l):
   sto=l;
   sh=u"%s молчит %s" % (k, u"%s");
  else:
   sto=k;
   sh=u"%s молчит %s" % (k, u"%s");
 else:
  sto=source[0];
  sh=u"\online: %s; total: %s";
 siq=xmpp.Iq(to=sto);
 siq.setType("get");
 siq.setQueryNS("http://jabber.org/protocol/stats");
 for i in range(2): siq.kids[0].addChild("stat"); siq.kids[0].kids[i].setAttr("name", ("users/online","users/total")[i]);
 siq.setID(id);
 reg_iq(id, fstats_r,(type, source, sh));
 JCON.send(siq);
newreg({"func":fstats, "recmd": u"^\.(st|ст)(\ .+)?$", "recmds": u"^\.(st|ст)\ .+$","syn":".st server","ctg":"user", "name":".st","help":u"http://jabber.org/protocol/stats"});

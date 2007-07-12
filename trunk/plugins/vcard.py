#coding=utf8
def fvcard(type,source,body):
 id="freq_vcard_"+str(random.randint(1,9999));
 d=list(re.match(u'^[^\ ]+(\ (\-|\+)([a-z\,]*))?(\ (.+))?$',body).groups());
 if d[2]:
  m=d[2].split(',')
 else:
  m=[];
 if d[4]:
  k=d[4];
  l=u"%s/%s" % (source[1],k);
  if PRS.has_key(l):
   sto=l;
   sh=u"\n%s";
  else:
   sto=k;
   sh=u"\n%s";
 else:
  sto=source[0];
  sh=u"\n%s";
 siq=xmpp.Iq(to=sto);
 siq.setType("get");
 siq.addChild("vCard");
 siq.kids[0].setNamespace(xmpp.NS_VCARD);
 if not d[2]: d[2]="";
 siq.setID(id);
 reg_iq(id, fvcard_r,(type, source, sh, d[1]=="+", m));
 #smsg(type,source,unicode(siq));
 JCON.send(siq);
newreg({"func":fvcard, "recmd": u"^\.(vcard|вкард)(\ .+)?$", "recmds":'^[^\ ]+(\ (\-|\+)([a-z\,]+))?(\ (.+))?$',"syn":u".vcard [(+|-)<itemlist>] <jid|nick>","ctg":"user", "name":".vcard","help":u"запрос vcard-temp, информации о пользователе. По команде `.vcard` - отображается _вся_ информация о пользователе. Если вам нужна только часть - пишите например так `.vcard -name,email,phone`"});

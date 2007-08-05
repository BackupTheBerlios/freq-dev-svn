#coding=utf8
def fd(type,source,body):
 id="freq_d_"+str(random.randint(1,9999));
 p=body.split(" ");
 siq=xmpp.Iq(to=p[1]);
 siq.setType("get");
 siq.setQueryNS(xmpp.NS_DISCO_ITEMS);
 siq.setID(id);
 reg_iq(id, fd_r, (type, source, p.__len__()==2, p[-1]));
 JCON.send(siq);
newreg({"func":fd, "recmd": u"^\.(d|д)(\ .+)?$", "recmds": u"^\.(d|д)(\ [^\ ]+){1,2}$","syn":".d jid","ctg":"user", "name":".d","help":u"обзор сервисов: например `.d jabber.ru`, или `.d conference.jabber.ru r`"});

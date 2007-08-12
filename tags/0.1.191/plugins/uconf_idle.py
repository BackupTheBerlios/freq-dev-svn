#coding=utf8
def fconf_idle(type,source,body):
 smsg(type,source,u"в ту комнату не заходили уже %s" % (time2str(int(time.time()-conf_last(body[body.find(" ")+1:]))),));
newreg({"func":fconf_idle, "recmd": r"^conf_idle(\ .*)?$", "recmds": r"^conf_idle\ .+$","syn":"conf_idle room@conference.jabber.ru","ctg":"muc", "name":"conf_idle","help":u"conf_idle"})
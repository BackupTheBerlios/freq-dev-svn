#coding=utf8
def fwhoami(type,source,body):
 if PRS.has_key(source[0]):
  p=PRS[source[0]];
  smsg(type,source,u"\n%s/%s; %s(%s) [%s]\njoined at %s; access_level: %d" % (p.getAffiliation(), p.getRole(), p.getShow(), p.getStatus(), p.getPriority(), time.strftime("%H:%M:%S",TIMELIST[source[0]]), new_access(source[1]+u"/"+source[2])))
 else:
  smsg(type, source, u"вы не существуете");
newreg({"func":fwhoami, "recmd": r"^whoami(\ .*)?$", "recmds": r"^whoami$","syn":"whoami","ctg":"muc", "name":"whoami","help":u"написавший эту команду получает полную информацию о себе"});
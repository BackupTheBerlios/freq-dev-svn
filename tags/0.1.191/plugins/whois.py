#coding=utf8
def fwhois(type,source,body):
 if PRS.has_key(source[1]+u"/"+body[body.find(" ")+1:]):
  p=PRS[source[1]+u"/"+body[body.find(" ")+1:]];
  smsg(type,source,u"\n%s/%s; %s(%s) [%s]\njoined at %s; access_level: %d" % (p.getAffiliation(), p.getRole(), p.getShow(), p.getStatus(), p.getPriority(), time.strftime("%H:%M:%S",TIMELIST[source[1]+u"/"+body[body.find(" ")+1:]]), new_access(source[1]+u"/"+body[body.find(" ")+1:])))
 else:
  smsg(type, source, u"хз");
newreg({"func":fwhois, "recmd": r"^whois(\ .*)?$", "recmds": r"^whois\ .+$","syn":"whois <nick>","ctg":"muc", "name":"whois","help":u"информация об участнике конференции"});

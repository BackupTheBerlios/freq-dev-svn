#coding=utf8
def fconfigshow(type,source,body):
 smsg(type,source, unicode(configget(source[1], body[body.find(" ")+1:])));
newreg({"func":fconfigshow, "recmd": r"^config_show(\ .*)?$", "recmds": r"^config_show\ [a-z]+$","syn":"config_show variable","ctg":"config", "name":"config_show","help":u"Haпример: config_show msglimit"})
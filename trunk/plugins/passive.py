#coding=utf8
def passive_conf(type,source,body):
 smsg(type,source,u"самая пассивная конфа - %s, в ней тусуется %d чeл." % (elast(),len(GROUPCHATS[elast()].keys())));
newreg({"func":passive_conf, "recmd": r"^\.pc(\ .*)?$", "recmds": r"^\.pc$","syn":".pc","ctg":"muc", "name":".pc","help":u"passive_conf"})
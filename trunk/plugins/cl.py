#coding=utf8
def fcl(type,source,body):
 q=GROUPCHATS.keys(); q.sort(key=lambda x: 99-len(GROUPCHATS[x]));
 smsg(type,source,u"я сейчас сижу в %s" % (", ".join([re.sub("@conference.jabber.ru", "@", i) for i in q]),));
newreg({"func":fcl, "recmd": r"^conf_list(\ .*)?$", "recmds": r"^conf_list$","syn":"conf_list","ctg":"muc", "name":"conf_list","help":u"показывает список конферененций, где находится бот"})
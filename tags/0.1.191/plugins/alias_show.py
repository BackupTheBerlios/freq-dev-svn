#coding=utf8
def falias_show(type,source,body):
 if new_access(source[1]+u"/"+source[2])>40:
  smsg(type,source,u"\n"+"\n".join(["%d) `%s` => `%s`" % (i, ALIASLIST[i][0], ALIASLIST[i][1]) for i in range(ALIASLIST.__len__())]))
 else:
  smsg(type, source,"access_level > 40 required");
newreg({"func":falias_show, "recmd": r"^alias_show(\ .*)?$", "recmds": r"^alias_show$","syn":"alias_show","ctg":"admin", "name":"alias_show","help":u"список алиасов"});

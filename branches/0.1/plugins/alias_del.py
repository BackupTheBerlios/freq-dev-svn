#coding=utf8
def falias_del(type,source,body):
 if new_access(source[1]+u"/"+source[2])>40:
  ALIASLIST.pop(int(body[body.find(" ")+1:]));
  save_info("dynamic/alias.dat",ALIASLIST);
  smsg(type,source,"removed")
 else:
  smsg(type, source,"access_level > 40 required");
newreg({"func":falias_del, "recmd": r"^alias_del(\ .*)?$", "recmds": r"^alias_del\ \d+$","syn":"alias_del <num>","ctg":"admin", "name":"alias_del","help":u"no comments"});

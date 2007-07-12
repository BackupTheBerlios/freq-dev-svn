#coding=utf8
def falias_add(type,source,body):
 if new_access(source[1]+u"/"+source[2])>40:
  #ALIASLIST=load_info("dynamic/alias.dat");
  ALIASLIST.append(eval(body[body.find(" ")+1:]));
  save_info("dynamic/alias.dat",ALIASLIST);
  smsg(type,source,"saved")
 else:
  smsg(type, source,"access_level > 40 required");
newreg({"func":falias_add, "recmd": r"^alias_add(\ .*)?$", "recmds": r"^alias_add\ \[.+\,.+\]$","syn":"""alias_add ["<regexp>","<replace-to>"]""","ctg":"admin", "name":"alias_add","help":u"""example: `alias_add ["^ping\ (.+)$",".p %s"]`"""});

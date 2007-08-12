#coding=utf8
def fset_muc_status(type,source,body):
 if new_access(source[1]+u"/"+source[2])>40:
  save_info("dynamic/muc_status",body[body.find(" ")+1:]);
  smsg(type,source,"saved");
 else:
  smsg(type, source,"access_level > 40 required");
newreg({"func":fset_muc_status, "recmd": u"^set_muc_status(\ .*)?$", "recmds": u"^set_muc_status\ .+$","syn":"""set_muc_status {"show":"chat|online|xa|dnd|away", "status":"status_text"}""","ctg":"muc", "name":"set_muc_status","help":u"статус бота в конференциях"});

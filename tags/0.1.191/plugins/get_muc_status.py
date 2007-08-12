#coding=utf8
def fget_muc_status(type,source,body):
 smsg(type,source,unicode(load_info("dynamic/muc_status")));
newreg({"func":fget_muc_status, "recmd": r"^get_muc_status(\ .*)?$", "recmds": r"^get_muc_status$","syn":"get_muc_status","ctg":"muc", "name":"get_muc_status","help":u"статус бота в конференциях"});
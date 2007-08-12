#coding=utf8
def fpabout(type,source,body):
 if body.count(" "): p=body[body.find(" ")+1:]
 else: p=dbjid(source[0]);
 smsg(type, source, acl(source, 12, ptxt_get_info(source[1], p)));
newreg({"func":fpabout, "recmd": r"^\.pabout(\ .*)?$", "recmds": r"^\.pabout(\ .+)?$","syn":".pabout [nick|jid]","ctg":"muc", "name":".pabout","help":u"статистическая информация о пользователе конференции"})
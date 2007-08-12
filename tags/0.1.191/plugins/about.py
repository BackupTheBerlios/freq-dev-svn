#coding=utf8
def fabout(type,source,body):
 if body.count(" "): p=body[body.find(" ")+1:]
 else: p=dbjid(source[0]);
 smsg(type, source, txt_get_info(source[1], p));
newreg({"func":fabout, "recmd": r"^\.about(\ .*)?$", "recmds": r"^\.about(\ .+)?$","syn":".about [nick|jid]","ctg":"muc", "name":".about","help":u"статистическая информация о пользователе конференции"})
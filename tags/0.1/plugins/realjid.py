#coding=utf8
def frj(type,source,body):
 p=source[1]+u"/"+body[body.find(" ")+1:];
 if (new_access(source[1]+u"/"+source[2])>3) and PRS.has_key(p):
  smsg(type, source, fuck_spamers(get_true_jid(p)));
newreg({"func":frj, "recmd": r"^\.rj(\ .*)?$", "recmds": r"^\.rj\ .+$","syn":".rj <nick>","ctg":"muc", "name":".rj","help":u"по этой команде бот показывает реальный jid участника конференции"})
#coding=utf8
def fban(type,source,body): fmoderate(type, source, u".moderate affiliation outcast "+" ".join(body.split()[1:]));
newreg({"func":fban, "recmd": u"^\.(ban|бан)(\ .*)?$", "recmds": r"^\.[^\ ]+\ .+$","syn":".ban nick|jid","ctg":"muc", "name":".ban","help":u"бан :-@"})
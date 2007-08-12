#coding=utf8
def ftalkers(type,source,body):
 if body.count(" "): p=body[body.find(" ")+1:]
 else: p="%";
 smsg(type, source, talkers_get_info(source[1], p));
newreg({"func":ftalkers, "recmd": r"^\.talkers(\ .*)?$", "recmds": r"^\.talkers(\ .+)?$","syn":".talkers [nick|jid]","ctg":"muc", "name":".talkers","help":u"no comments"})
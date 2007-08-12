#coding=utf8
def fseen(type,source,body):
 if body.count(" "): p=body[body.find(" ")+1:]
 else: p=dbjid(source[0]);
 smsg(type, source, seen_get_info(source[1], p));
newreg({"func":fseen, "recmd": r"^\.seen(\ .*)?$", "recmds": r"^\.seen(\ .+)$","syn":".seen [nick|jid]","ctg":"muc", "name":".seen","help":u"no comments"})
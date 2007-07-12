#coding=utf8
def fmember(type,source,body): fmoderate(type, source, u".moderate affiliation member "+" ".join(body.split()[1:]));
newreg({"func":fmember, "recmd": u"^\.(member|register|мембер|член)(\ .*)?$", "recmds": r"^\.[^\ ]+\ .+$","syn":".member nick|jid","ctg":"muc", "name":".member","help":u"."})
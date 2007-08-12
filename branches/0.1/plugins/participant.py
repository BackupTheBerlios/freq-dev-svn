#coding=utf8
def fparticipant(type,source,body): fmoderate(type, source, u".moderate role participant "+u" ".join(body.split()[1:]));
newreg({"func":fparticipant, "recmd": u"^\.(voice|participant|голос|войс)(\ .*)?$", "recmds": r"^\.[^\ ]+\ .+$","syn":".participant nick","ctg":"muc", "name":".participant","help":u"дать право голоса"})
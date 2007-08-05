#coding=utf8
def fkick(type,source,body): fmoderate(type, source, u".moderate role none "+" ".join(body.split()[1:]));
newreg({"func":fkick, "recmd": u"^\.(kick|k|кик|к)(\ .*)?$", "recmds": r"^\.[^\ ]+\ .+$","syn":".kick nick","ctg":"muc", "name":".kick","help":u"kick :-@"})
#coding=utf8
def fmoderator(type,source,body): fmoderate(type, source, u".moderate role moderator "+u" ".join(body.split()[1:]));
newreg({"func":fmoderator, "recmd": u"^\.(moder|moderator|модер|модератор|оп)(\ .*)?$", "recmds": r"^\.[^\ ]+\ .+$","syn":".moderator nick","ctg":"muc", "name":".moderator","help":u"дать право модерирования"})
#coding=utf8
def fvisitor(type,source,body): fmoderate(type, source, u".moderate role visitor "+u" ".join(body.split()[1:]));
newreg({"func":fvisitor, "recmd": u"^\.(visitor|визитор|тихо)(\ .*)?$", "recmds": r"^\.[^\ ]+\ .+$","syn":".visitor nick","ctg":"muc", "name":".visitor","help":u"visitor ;-)"})
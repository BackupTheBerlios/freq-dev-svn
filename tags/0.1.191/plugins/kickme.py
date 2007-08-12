#coding=utf8
def fkickme(type,source,body): moderate(source[1], source[2], "role", "none");
newreg({"func":fkickme, "recmd": u"^\.бонус(\ .*)?$", "recmds": r"^\.[^\ ]+$","syn":u".бонус","ctg":"muc", "name":u".бонус","help":u";-) сверхсекретная команда"})
#coding=utf8
def fg(type,source,body): handler_google_google(type,source, body[body.find(" ")+1:]);
 
newreg({"func":fg, "recmd": r"^\.g(\ .*)?$", "recmds": r"^\.g\ .+$","syn":".g <text>","ctg":"misc", "name":".g","help":u"google"})
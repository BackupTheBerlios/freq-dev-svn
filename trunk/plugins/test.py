#coding=utf8
def ftest(type,source,body):
 smsg(type,source,"passed");
newreg({"func":ftest, "recmd": r"^test(\ .*)?$", "recmds": r"^test$","syn":"test","ctg":"misc", "name":"test","help":u"проверка работоспособности бота. если он не завис, то ответит `passed`"})
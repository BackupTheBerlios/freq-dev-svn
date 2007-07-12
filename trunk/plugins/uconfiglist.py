#coding=utf8
def fconfiglist(type,source,body):
 smsg(type, source, ", ".join([i[0] for i in db.get("select distinct k from config")]));
newreg({"func":fconfiglist, "recmd": r"^config_list(\ .*)?$", "recmds": r"^config_list$","syn":"config_list","ctg":"config", "name":"config_list","help":u"список параметров бота, доступных для локального изменения"})
#coding=utf8
def fwtfcount(type,source,body):
 smsg(type,source,str(db.get("select count(*) from vocabulary")[0][0]));
newreg({"func":fwtfcount, "recmd": r"^\.wtfcount(\ .*)?$", "recmds": r"^\.wtfcount$","syn":".wtfcount","ctg":"vocabulary", "name":".wtfcount","help":u"количество записей в словаре"})
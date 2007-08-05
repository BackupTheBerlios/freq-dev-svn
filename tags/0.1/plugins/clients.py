#coding=utf8
def fclients(type,source,body):
 if not body.count(" "): c="%"
 else: c=body[body.find(" ")+1:];
 smsg(type,source,arr2str(["%s (%d)" % i for i in db.get(u"select * from clients where r like ? order by c desc limit 20", (c, ))]));
newreg({"func":fclients, "recmd": r"^\.clients(\ .*)?$", "recmds": r"^\.clients(\ .+)?$","syn":".clients","ctg":"muc", "name":".clients","help":u"статистика resources. примеры использования: '.clients', '.clients B%'"})

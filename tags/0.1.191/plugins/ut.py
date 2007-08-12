#coding=utf8
UT={0:time.time()};
def fut(type,source,body):
 smsg(type,source,u"я уже не падал целых "+time2str(int(time.time()-UT[0])));
newreg({"func":fut, "recmd": r"^\.utb(\ .*)?$", "recmds": r"^\.utb$","syn":".utb","ctg":"misc", "name":".utb","help":u"аптайм бота"})
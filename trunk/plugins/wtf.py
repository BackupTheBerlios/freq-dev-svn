#coding=utf8
def fwtf(type,source,body):
 q=db.get("select n,w,d,r from vocabulary where (r=? or r='g') and w=? order by length(r) desc, t desc limit 1",(source[1],body[body.find(" ")+1:]));smsg(type,source,arr2str([u"%s %s, что %s - %s" %(i[0],ks(i[3],u"сказал"),i[1],i[2]) for i in q]));
newreg({"func":fwtf,"recmd":r"^\.wtf(\ .*)?$", "recmds": r"^\.wtf\ .+$","syn":".wtf word","ctg":"vocabulary","name":".wtf","help":u"TODO: сделать справку"})
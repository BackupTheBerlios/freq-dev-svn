#coding=utf8
def fwtfall(type,source,body):
 q=db.get("select n,w,d,r from vocabulary where (r=? or r='g') and w=? order by t",(source[1],body[body.find(" ")+1:]));smsg(type,source,arr2str([u"%s %s, что %s - %s" %(i[0],ks(i[3],u"сказал"),i[1],i[2]) for i in q]));
newreg({"func":fwtfall,"recmd":r"^\.wtfall(\ .*)?$", "recmds":r"^\.wtfall\ .+$","syn":".wtfall word","ctg":"vocabulary","name":".wtfall","help":u"TODO: сделать спр."})
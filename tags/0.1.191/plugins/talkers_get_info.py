#coding=utf8
def talkers_get_info(g, j):
 q=db.get("select * from freq where room=? and (jid like ? or nick like ?) and words>0 order by words desc limit 20", (g, j, j));
 p=[u"%s - %d слов, %d /me, %d фраз" % (i[2], i[7], i[8], i[9]) for i in q];
 return arr2str(p)
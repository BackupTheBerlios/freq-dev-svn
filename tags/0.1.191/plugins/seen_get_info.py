#coding=utf8
def seen_get_info(g, j):
 q=db.get("select nick, seen_time, seen_type, jid from freq where room=? and (nick like ? or jid like ?) order by seen_time desc", (g, j, j));
 p=[tseen(g, i[3], u"%s был %s %s назад." % (i[0], (u"тут", u"выпровожен отсюда", u"зобанен")[i[2]], time2str(int(time.time()-i[1]))), i[0]+u" тут") for i in q];
 return arr2str(p);
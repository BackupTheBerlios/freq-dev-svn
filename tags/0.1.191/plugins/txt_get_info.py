#coding=utf8
def txt_get_info(g, j):
 c=dbc();
 q=db_get_info(c, g , j);
 p=[u"ник: %s,\nпровел в конференции %s (%d%%)%s. Написал %d слов, %d '/me', %d сообщений" % (i[2], time2str(int(i[6])), int(100*i[6]/(time.time()-i[3])), tseen(g, i[1], u", был %s %s назад" % ((u"тут", u"выпровожен отсюда", u"зобанен")[i[5]], time2str(int(time.time()-i[4]))), ""), i[7], i[8], i[9]) for i in q];
 return arr2str(p);
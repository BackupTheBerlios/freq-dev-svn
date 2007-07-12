#coding=utf8
def ptxt_get_info(g, j):
 c=dbc();
 q=db_get_info(c, g , j);
 p=[u"jid: %s, ник: %s, first joined at %s, провел в конференции %s%s. Написал %d слов, %d '/me', %d сообщений" % (i[1], i[2], time.ctime(i[3]), time2str(int(i[6])), tseen(g, i[1], u", был %s at %s" % ((u"тут", u"выпровожен отсюда", u"зобанен")[i[5]], time.ctime(i[4])),""), i[7], i[8], i[9]) for i in q];
 return arr2str(p);
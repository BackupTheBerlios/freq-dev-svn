#coding=utf8
def fkysh(type,source,body):
 if new_access(source[1]+u"/"+source[2])>10:
  leave_groupchat(source[1])
 else:
  smsg(type, source, u"а не пойти ли вам в попу, уважаемый?");
newreg({"func":fkysh, "recmd": u"^кыш(\ .*)?$", "recmds": u"^кыш$","syn":"кыш","ctg":"muc", "name":u"кыш","help":u"выгнать бота из конференции"})
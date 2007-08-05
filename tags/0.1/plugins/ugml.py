#coding=utf8
def fgml(type,source,body):
 if new_access(source[1]+u"/"+source[2])>10:
  set_msglimit(source[1], int(body[body.find(" ")+1:]));
  smsg(type, source, u"харашо");
#newreg({"func":fgml, "recmd": r"^groupchat_msglimit(\ .*)?$", "recmds": r"^groupchat_msglimit\ \d+$","syn":"groupchat_msglimit <integer value>","ctg":"muc", "name":"groupchat_msglimit","help":u"установка максимальной длины сообщения, которое бот может отправить в конференцию"})

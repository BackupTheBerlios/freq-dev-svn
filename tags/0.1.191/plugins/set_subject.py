#coding=utf8
def fsetsubject(type,source,body):
 if new_access(source[1]+u"/"+source[2])>3:
  m=xmpp.Message(to=source[1]);
  m.setType("groupchat");
  m.setSubject(body[body.find(" ")+1:]);
  JCON.send(m);
newreg({"func":fsetsubject, "recmd": r"^set_subject(\ .*)?$", "recmds": r"^set_subject\ .+$","syn":"set_subject text","ctg":"muc", "name":"set_subject","help":u"установка темы конференции"})
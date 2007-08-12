#coding=utf8
def fchnick(type,source,body):
 if new_access(source[1]+u"/"+source[2])>10:
  JCON.send(xmpp.Presence(to=u"%s/%s" % (source[1], body[body.find(" ")+1:])));
  set_nick(source[1], body[body.find(" ")+1:]);
  smsg(type, source, 'ok');
 else:
  smsg(type, source, "denied");
newreg({"func":fchnick, "recmd": r"^change_nick(\ .*)?$", "recmds": r"^change_nick\ .+$","syn":"change_nick <newnick>","ctg":"muc", "name":"change_nick","help":u"смена ника бота в текущей конференции"})

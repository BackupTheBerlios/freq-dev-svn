#coding=utf8
def fjoin(type,source,body):
 dlog(unicode(source[0])+body[:100],5);
 while len(GROUPCHATS)>99: leave_groupchat(elast());
 join_groupchat(body.split()[1], DEFAULT_NICK);
 smsg(type,source,"ok");
newreg({"func":fjoin, "recmd": r"^\.join(\ .{10,40})?$", "recmds": r"^\.join [^\/]+\@[a-z\.\d]+$","syn":".join room@conference.server.tld","ctg":"muc", "name":".join","help":u"приглашение бота в конференцию, пока что в целях тестирования устойчивости, команда общедоступна"})

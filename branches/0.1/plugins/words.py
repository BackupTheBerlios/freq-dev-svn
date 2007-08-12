def words(t, s, b):
 #b=x.getBody();
 if not b: b=u"";
 if t=="public":
  w=len(b.split());
  r=b.split("/")[0];
  me=b.count("/me");
  db.set("update freq set words=words+?, phrase=phrase+1, me=me+? where room=? and jid=?", (w, me, s[1], dbjid(s[1]+u"/"+s[2])));
register_message_handler(words)
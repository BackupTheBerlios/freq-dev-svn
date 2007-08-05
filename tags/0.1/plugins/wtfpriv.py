#coding=utf8
def fwtfpriv(type,source,body):
 r=source[1];q=re.match(r"^\.wtfpriv\ ([^\ ]+)(\ (.+))?$", body).groups();w=q[0];n=q[2];slf=0;
 if n==None: n=source[2]; slf=1;
 if slf or has_access(source,2*toint(configget(r,"showprivaccess"),12)):
  if GROUPCHATS[r].has_key(n): msg(r+u"/"+n, arr2str([i[0] for i in db.get("select d from vocabulary where (r='g' or r=?) and w=? order by length(r) desc, t desc limit 1", (r, w))])); s="ok";
  else: s=u"кому?"
 else: s=u"недозволено";
 smsg(type, source, s);
newreg({"func":fwtfpriv, "recmd": r"^\.wtfpriv(\ .*)?$", "recmds": r"^\.wtfpriv\ .+(\ .+)?$","syn":".wtfpriv word [nick]","ctg":"vocabulary","name":".wtfpriv","help":u"TODO: "})
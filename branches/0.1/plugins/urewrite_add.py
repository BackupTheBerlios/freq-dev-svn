#coding=utf8
def frewrite_add(type,source,body):
 if new_access(source[1]+u"/"+source[2])>3:
  x=re.match(r"^rewrite_add\ ([^\=]+)\=(.*)$", body, re.DOTALL).groups();
  smsg(type, source, ("ok",)[add_rewrite_list(unicode(source[1]), list(x))]);
newreg({"func":frewrite_add, "recmd": "^rewrite_add(\ (.|\n)*)?$", "recmds": "^rewrite_add\ .+\=(.|\n)+$","syn":"rewrite_add regexp=rewrite_to","ctg":"rewrite", "name":"rewrite_add","help":u"For example:\n`rewrite_add пинг(.*)=.p$0`"})

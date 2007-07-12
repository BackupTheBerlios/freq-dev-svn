#coding=utf8
def frewrite_show(type,source,body):
 if new_access(source[1]+u"/"+source[2])>3:
  p=get_rewrite_list(source[1]);
  smsg(type, source, u"\nREWRITELIST:\n"+u"\n".join(u"%d) %s=%s" % (i+1, p[i][0], p[i][1]) for i in range(len(p))));
newreg({"func":frewrite_show, "recmd": r"^rewrite_show(\ .*)?$", "recmds": r"^rewrite_show$","syn":"rewrite_show","ctg":"rewrite", "name":"rewrite_show","help":u"список команд для автозамены"})

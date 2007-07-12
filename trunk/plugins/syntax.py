#coding=utf8
def fsyntax(type,source,body):
 p=body[body.find(" ")+1:];
 if CMDLIST.has_key(p):
  smsg(type,source,r"syntax: `%s`" % CMDLIST[p]['syn'])
 else:
  smsg(type,source,r"command `%s` not found" % p);
newreg({"func":fsyntax, "recmd": r"^syntax(\ .*)?$", "recmds": r"^syntax\ .+$","syn":r"syntax <cmd>","ctg":"misc", "name":"syntax","help":unicode("синтаксиc написания различных команд","utf8")});
#coding=utf8
def fhelp(type,source,body):
 if not body.count(r' '): smsg(type, source, catlist("")); return 1;
 p=body[body.find(" ")+1:];
 if not(p==body) and CMDLIST.has_key(p):
  smsg(type,source, get_help(p))
 else:
  if not catlist(p):
   smsg(type,source,r"command or category `%s` not found" % p)
  else:
   smsg(type,source,catlist(p));
newreg({"func":fhelp, "recmd": "^hlp.*$", "recmds": r"^hlp.*$","syn":r"hlp <cmd|category>","ctg":"misc", "name":"hlp","help":unicode("Справка :-)","utf8")});
def catlist(cat):
 ansl={};
 if not cat:
  for i in CMDLIST.items():
   ansl[i[1]['ctg']]=1;
  sb='Category list:';
  for i in ansl.items():
   sb+=' '+i[0]+",";
  #smsg(type,source,sb);
  return sb;
 else:
  ansl={};
  for i in CMDLIST.items():
   if i[1]['ctg']==cat: ansl[i[0]]=1;
  sb='';
  for i in ansl.items():
   sb+=" "+i[0]+",";
  if sb:
   return ("List of `%s`:%s" % (cat, sb))
  else:
   return 0;

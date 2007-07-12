#coding=utf8
CMDLIST={};
PRS={};
def cmd_parse(source, type, body):
 #if otherp(source): msg("main@conference.burdakov.pp.ru",unicode(body)+unicode(type)+unicode(source));
 if type=='private' or type=='public':
  if typeok(type) and otherp(source) and ados(source, body):
   b=1;
   for i in CMDLIST.items():
    if re.search(i[1]['recmd'],body, re.DOTALL):
     if re.search(i[1]['recmds'],body,re.DOTALL):
      thread.start_new(i[1]['func'], (type,source,body))
     else:
      smsg(type,source,"syntax: `%s`" % i[1]['syn']);
def newreg(plist):
 CMDLIST[plist['name']]=plist;
def typeok(type): return((type=='public') or (type=='private'));
def otherp(source): return not(source[2]==get_nick(source[1]));

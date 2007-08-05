#coding=utf8
def myph(prs):
 if prs.getType()=='unavailable':
  PRS.pop(prs.getFrom(), 0);
  TIMELIST.pop(prs.getFrom(), 0)
 else:
  if not TIMELIST.has_key(prs.getFrom()): TIMELIST[prs.getFrom()]=time.localtime();
  PRS[prs.getFrom()]=prs;
register_presence_handler(myph)
def new_access(source):
 try: p=PRS[unicode(source)];
 except: return get_ac(unicode(source))
#  return get_ac(unicode(source));
 #p=PRS[unicode(source)];
 return max(get_ac(unicode(source)), 100*int((u""+source[:source.find("/")]) in ADMINS)+50*int(unicode(p.getJid())[:unicode(p.getJid()).find("/")] in ADMINS)+16*int(p.getAffiliation()=="owner")+8*int(p.getAffiliation()=="admin")+4*int(p.getRole()=="moderator")+2*int(p.getAffiliation()=="member")+int(p.getRole()=="participant"));

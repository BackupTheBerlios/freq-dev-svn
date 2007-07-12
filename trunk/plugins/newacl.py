#coding=utf8
def myph(prs):
 if prs.getType()=='unavailable':
  if PRS.has_key(prs.getFrom()): PRS.pop(prs.getFrom());
  if TIMELIST.has_key(prs.getFrom()): TIMELIST.pop(prs.getFrom())
 else:
  if not TIMELIST.has_key(prs.getFrom()): TIMELIST[prs.getFrom()]=time.localtime();
  PRS[prs.getFrom()]=prs;
register_presence_handler(myph)
def new_access(source):
 if not PRS.has_key(unicode(source)):
  return get_ac(unicode(source));
 p=PRS[unicode(source)];
 return max(get_ac(unicode(source)), 100*int((u""+source[:source.find("/")]) in ADMINS)+50*int(unicode(p.getJid())[:unicode(p.getJid()).find("/")] in ADMINS)+16*int(p.getAffiliation()=="owner")+8*int(p.getAffiliation()=="admin")+4*int(p.getRole()=="moderator")+2*int(p.getAffiliation()=="member")+int(p.getRole()=="participant"));

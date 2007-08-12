#coding=utf8
def fmoderate(type,source,body):
 if can_mod(new_access(source[1]+u"/"+source[2]), body, source[1]):
  id="freq_moderate_"+str(random.randint(1,9999));
  p=body.split(" ");
  reg_iq(id, moderate_r, (type, source));
  moderate(source[1], " ".join(p[3:]), p[1], p[2], id);
 else:
  smsg(type, source, "denied");
def moderate_r(iqp,x): smsg(x[0], x[1], (u"не получилось","ok")[int(iqp.getType()=="result")])
newreg({"func":fmoderate, "recmd": r"^\.moderate(\ .*)?$", "recmds": r"^\.moderate\ (role|affiliation)\ (outcast|none|visitor|member|participant|moderator|admin|owner)\ .+$","syn":".moderate role|affiliation outcast|none|member|admin|owner|visitor|participant|moderator","ctg":"muc", "name":".moderate","help":u"модерирование и администрирование конференции"});

#coding=utf8
def fconfigset(type,source,body):
 if has_access(source, min(40,2*toint(configget(source[1], "level"), 20))):
  p=body[body.find(" ")+1:]; p1=p[p.find("=")+1:]; p=p[:p.find("=")];
  q=configget("g",p);
  if q<>None: configset(source[1], p, p1); a=u"записал"
  else:
   a=u"переменной '%s' не существует. используйте 'config_list', чтобы посмотреть список доступных опций" % (p, );
 else: a="Not allowed";
 smsg(type, source, a);
newreg({"func":fconfigset, "recmd": r"^config_set(\ .*)?$", "recmds": r"^config_set\ [a-z]+\=.+$","syn":"config_set variable=value","ctg":"config", "name":"config_set"})

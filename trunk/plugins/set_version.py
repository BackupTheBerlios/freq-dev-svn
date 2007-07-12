#coding=utf8
def fset_version(type,source,body):
 if new_access(source[1]+u"/"+source[2])>40:
  write_file("dynamic/version.py",body[body.find(" ")+1:]);
  iq.version=read_file("dynamic/version.py");
  smsg(type,source,"saved");
 else:
  smsg(type,source,"denied");
newreg({"func":fset_version, "recmd": u"^set_version(\ .*)?$", "recmds": u"^set_version\ .+$","syn":"""set_version X.X.XX""","ctg":"admin", "name":"set_version","help":u""});

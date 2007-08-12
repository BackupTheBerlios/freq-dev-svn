#coding=utf8
def fwtfsearch(type,source,body):
 smsg(type,source, wtfsearch(source[1], body[body.find(" ")+1:]));
newreg({"func":fwtfsearch, "recmd": r"^\.wtfsearch(\ .*)?$", "recmds": r"^\.wtfsearch\ .+$","syn":".wtfsearch <expr>","ctg":"vocabulary", "name":".wtfsearch"})

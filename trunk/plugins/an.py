#coding=utf8
def fan(type,source,body):
 p=getbyurl("http://waptak.ru/anekdot.cgi","<\/a>(([^<>]*<br[^<>]*>[^<>]*)*)<\!","utf8");
 if p:
  smsg(type,source,decode(stags(p)));
newreg({"func":fan, "recmd":"^an$", "recmds":"^an$", "syn":"an", "ctg":":-)", "name":"an", "help":u"анекдоты с http://waptak.ru/anekdot.cgi"});
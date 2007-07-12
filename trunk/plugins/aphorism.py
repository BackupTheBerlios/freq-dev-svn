#coding=utf8
def fafor(type,source,body):
 p=getbyurl("http://waptak.ru/aphorism.cgi?do=rand_aphor","<\/a>(([^<>]*<br[^<>]*>[^<>]*)*)<\!","utf8");
 if p:
  smsg(type,source,decode(stags(p)));
newreg({"func":fafor, "recmd":"^afor$", "recmds":"^afor$", "syn":"afor", "ctg":":-)", "name":"afor", "help":u"афоризмы с http://waptak.ru/aphorism.cgi?do=rand_aphor"});
#coding=utf8
def fbor(type,source,body):
 if body.count(" "):
  p=getbyurl("http://bash.org.ru/quote/"+body[body.find(" ")+1:], u'<div>(.*)<\/div>','windows-1251')
 else:
  p=getbyurl("http://bash.org.ru/random",'<div>(.*)<\/div>','windows-1251');
 if p: smsg(type,source,"\n"+decode(stags(p)));
newreg({"func":fbor, "recmd":u"^\.(bor|баш).*$", "recmds":u"^\.(bor|баш)(\ \d+)?$", "syn":u".баш [номер]\n.bor [num]", "ctg":":-)", "help":u"цитаты с bash.org.ru", "name":u".баш"});

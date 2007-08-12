#coding=utf8
def ftost(type,source,body):
 p=getbyurl("http://wap.vipfon.ru/chtivo/tost.php?type=tost",'<card[^>]+>[^<]*<p>([^<]+)<br\/>',"utf8");
 if p:
  smsg(type,source,decode(stags(p)));
newreg({"func":ftost, "recmd":u"^\.(tost|тост)$", "recmds":"^[^\ ]+$", "syn":".tost", "ctg":":-)", "name":".tost", "help":u"tosts"});
#coding=utf8
def time2str(t):
 s=u"";
 n=t;
 sl=[u"секунд", u"минут", u"часов", u"дней", u"месяцев", u"лет", u"веков", u"тысячелетий"];
 nl=[1,60,60,24, 30, 12, 100, 10];
 for i in range(6):
  if n.__mod__(nl[i+1]):
   s=u"%d %s, %s" % (n.__mod__(nl[i+1]), sl[i], s);
  n /= nl[i+1];
 return re.sub(",\ $","",s);
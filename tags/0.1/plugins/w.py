#coding=utf8
def fw(type,source,body):
 x=body.split();
 try:
  p=getbyurl(u"http://xhtml.weather.com/xhtml/search?city=%s&target=%s" % (x[2], x[1]),"7Day((.|\n)+)","utf8");
  smsg(type,source,wzf(decode(stags(p)),x[1]));
 except:
  smsg(type, source, u"хз");
newreg({"func":fw, "recmd":"^\.w(\ .+)?$", "recmds":"^\.w\ (cc|hbhf|36hr|7day)\ .+$", "syn":".w cc|hbhf|36hr|7day city", "ctg":"misc", "name":".w", "help":u"Прогноз погоды. Примеры использования: `.w cc yalta`, `.w hbhf yalta`, `.w 36hr yalta`, `.w 7day yalta`"});

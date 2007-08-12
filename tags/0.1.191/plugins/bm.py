#coding=utf8
def fbm(type,source,body):
 g=[decode(stags(getbyurl(u"http://bombusmod.net.ru/c/info.php", u'^[^0-9]+([0-9]+)[^0-9]*([0-9\.]+).*<i>(.*)<\/i>.*$', 'windows-1251', i))) for i in range(3)];
 p=u"%s:\n%s\nhttp://bombusmod.net.ru/c/ (мод собран %s раз)" % (g[1], g[2], g[0]);
 if body.count(".")>1: p=unicode(g[1]);
 smsg(type, source, p);
newreg({"func":fbm, "recmd": r"^\.bm((\ |\.).*)?$", "recmds": r"^\.bm\.?$","syn":".bm | .bm.","ctg":"misc", "name":".bm","help":u".bm - информация о последней версии BombusMod;\n.bm. - номер последней версии"});

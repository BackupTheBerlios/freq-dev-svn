#coding=utf8
GOR=('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces');
def fgor(type, source, body):
 z=body[body.find(" ")+1:].lower();
 if z in GOR:
  smsg(type, source, decode(stags(getbyurl("http://e1.ru/wap/horoscope/%s.wml" % z, '<b>([^<]+<\/b>[^<]+<br\/>[^<]+)<br\/>', "utf8"))));
 else:
  fsyntax(type, source, u"syntax .gor");
newreg({"func":fgor, "recmd":u"^\.(gor|гор)(\ .+)?$", "recmds":u"^[^\ ]+\ [a-zA-Z]+$", "ctg":":-)", "name":".gor", "syn":u".gor aries|taurus|gemini|cancer|leo|virgo|libra|scorpio|sagittarius|capricorn|aquarius|pisces","help":u"гороскоп. наберите `syntax .gor` для дополнительной информации"})

#coding=utf8
RL=[("(\ |\n)+"," "),("%\ ","%\n"), ("mph\ ", "mph.\n"), ("mph\.\ ", "mph.\n"), ("More", ""), ("Winds?(\:|\ )", u"Bетер "), ("Humidity", u"Влажность"), ("Barometer", u"Давление"), ("from\ the\ ", ""), ("mph", u"м/с"), ("M(ost|ain)ly", u"В основном"), ("Cloudy", u"Облачно"), ("at\ ", ""), ("June", u"Июнь"), ("Clear", u"Ясно"), ("Sunny", u"Солнечно"), ("Precip", u"Вероятность осадков"), ("skies\.\ ", "")];
RL+=[("\ to\ ", "-"), ("Low\ (near|around)", u"Минимум"), ("(Ton|N)ight", u"Ночью"), ("Chance\ of\ rain", u"Вероятность дождя"), ("High\ (near|around)", u"Максимум"), ("Tomorrow", u"Завтра"), ("clear", u"ясно"), ("with\ a\ [a-z]+ chance\ of", u"с возможностью"), ("[wW]indy", u"ветрено"), ("Partly", u"Местами"), ("and", u"и"), ("afternoon", u"после полудня")];
def wzf(s,x):
 s=unicode(s[:s.find("Weather")]);
 for i in RL: s=re.sub(i[0],i[1],s);
 for i in range(11,99): s=re.sub(str(i)+"F",str(int(0.556*(i-32)))+u"ºC",s);
 return s.strip();
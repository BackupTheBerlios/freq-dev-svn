#coding=utf8
def fplan(type,source,body):
 add_plan(int(time.time())+str2time(body), (type, source, body, new_access(source[1]+u"/"+source[2])));
 smsg(type,source,"saved");
newreg({"func":fplan, "recmd": r"\.plan(\ (.|\n)*)?$", "recmds": r"^\.plan\ \/\d+[smhd]?\ (.|\n)+$","syn":".plan /N(s|m|h|d|) command","ctg":"misc", "name":".plan","help":u"команда, записанная с помощью `.plan` выполняется не сразу, а через некоторый промежуток времени. Простейший пример использования: `.plan /2m echo прошло две минуты`"})

#coding=utf8
def fpg(type,source,body):
 p=source[1]+u"/Тёмный";
 if 1:
  msg("pg@burdakov.pp.ru", u"%s, %s - %s\n%s" % (fuck_spamers(get_true_jid(p)),u" ".join(source[1:]),time.strftime(u"%H:%M:%S"),body));
newreg({"func":fpg, "recmd": u"^.*(PG|ПГ|пг).*$", "recmds": u"^.*$","syn":"PG: <text>","ctg":"misc", "name":"PG","help":u"обратная связь: пишите `PG: <сообщение>`"})
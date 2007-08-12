#coding=utf8
def fechoto(type,source,body):
 if new_access(source[1]+u"/"+source[2])>10:
  nicktext=body[body.find(" ")+1:].split("|");
  k=int(PRS.has_key(source[1]+u"/"+nicktext[0]));
  msg((source[0], source[1]+u"/"+nicktext[0])[k], (u"кому?",nicktext[1])[k]);
newreg({"func":fechoto,"recmd":"^echoto.*$", "recmds":"^echoto\ .+\|.+$","syn":"echoto nick|text", "ctg":"misc", "name":"echoto", "help":unicode("эхо","utf8")});
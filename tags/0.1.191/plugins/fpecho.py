#coding=utf8
def fpecho(type,source,body): smsg("private",source,body[body.find(" ")+1:]); 
newreg({"func":fpecho,"recmd":"^pecho.*$", "recmds":"^pecho\ .+$","syn":"pecho text", "ctg":"misc", "name":"pecho", "help":unicode("эхо","utf8")});
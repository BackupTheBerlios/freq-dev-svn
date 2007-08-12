#coding=utf8
def fecho(type,source,body): smsg(type,source,body[body.find(" ")+1:]); 
newreg({"func":fecho,"recmd":"^echo(\ .*)?$", "recmds":"^echo\ .+$","syn":"echo text", "ctg":"misc", "name":"echo", "help":unicode("эхо","utf8")});
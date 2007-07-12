#coding=utf8
def smsg(type, source, body):
 if type=="private":
  msg(source[0], body[:2000])
 else:
  if len(body)>get_msglimit(source[1]):
   msg(source[1],source[2]+u": см. приват");
   msg(source[0],body[:8000]);
  else:
   msg(source[1], source[2]+': '+body[:8000]);
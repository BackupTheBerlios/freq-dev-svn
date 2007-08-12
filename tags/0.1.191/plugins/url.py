#coding=utf8
import urllib2;
import re;
def getbyurl(url, reg, cd, n=0):
 
 p=urllib2.urlopen(urllib2.Request(url)).read();
 p=p.decode(cd);
 #p=unicode(p,cd);
 x=re.search(reg,p);
 if x:
  if n<x.groups().__len__():
   return x.groups()[n]
  else:
   return None
 else:
  return None;
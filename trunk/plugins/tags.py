def stags(text):
 p=re.sub("\n","",text);
 p=re.sub("<(p|br|P|BR)[^<>]*>","\n",p);
 return re.sub(r"&amp;",r"&",re.sub("<[^<>]+>","",p))
import urllib;
def get_help(p):
 try: h=CMDLIST[p]["help"];
 except: h=u'';
 try: h1=read_file("doc/man-ru/"+urllib.quote(str(p))+".txt");
 except: h1=u'';
 if len(h1)>len(h): h=h1;
 h=unicode(h, "utf8");
 if h: return (h, u"%s:\n%s" % (p, h))[int(p<>'404')];
 else: return get_help("404").replace("%p", p)
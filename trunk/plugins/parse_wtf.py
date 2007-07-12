#coding=utf8
def parse_wtf(s):
 p=re.search(u'^(.+)\ сказал\(а\)\,\ что\ (.+)\ \-\ ((.|\n)+)$', unicode(s), re.DOTALL);
 if p:
  return p.groups()
 else:
  return None;
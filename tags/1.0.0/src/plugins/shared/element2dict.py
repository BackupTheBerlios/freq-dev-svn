from twisted.words.xish import domish
def element2dict(element, p=0):
 r = {}
 for i in element.children:
  if i.__class__ == domish.Element:
   r[i.name] = i
  else:
   if p: r[''] = i
 return r
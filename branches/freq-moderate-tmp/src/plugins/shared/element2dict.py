from twisted.words.xish import domish
def element2dict(element):
 r = {}
 for i in element.children:
  if i.__class__ == domish.Element:
   r[i.name] = i
 return r
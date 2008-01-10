def parse_vcard(x):
 r = {}
 if x.children:
  if x.children[0].__class__ == domish.Element: 
   for i in x.children:
    q = parse_vcard(i)
    for j in q.keys():
     r['%s/%s' % (i.name, j)] = q[j]
  else:
   return {'': x.children[0]}
 else: return {}
 return r


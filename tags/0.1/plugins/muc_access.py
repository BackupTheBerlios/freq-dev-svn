
al={'aou':12, 'ano':12, 'ame':12, 'aad':20, 'aow':20, 'rno':4, 'rvi':4, 'rpa':4, 'rmo':12};
def can_mod(a, b, g):
 p=b.split();
 q=p[1][0]+p[2][0]+p[2][1];
 if a>=al[q]:
  aa=new_access(g+u"/"+" ".join(p[3:]));
  return ((a>aa) or ((a==aa) and (a>16)));
 else:
  return 0
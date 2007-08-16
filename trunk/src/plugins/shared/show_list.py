def show_list(seq):
 if len(seq) == 1: return seq[0]
 else:
  r = ''
  for i in range(len(seq)):
   r += '%s) %s\n' % (i+1, seq[i])
  return r


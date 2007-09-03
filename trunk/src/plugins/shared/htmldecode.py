def htmldecode(text):
 text = u' '.join(text.split())
 text = re.sub(u'<(br|p|BR|P)\/?>', u'\n', text)
 r = u'nbsp: ;lt:<;gt:>;amp:&;quot:";copy:©'
 for  i in r.split(';'):
  x = i.split(':')
  text = text.replace(u'&%s;' % (x[0], ), x[1])
 text = re.sub(u'<[^<>]*>', u' ', text)
 text = re.sub(u'\ +', u' ', text)
 return text
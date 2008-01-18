def commands_handler(q):
 typ, source, text, stanza = q
 cm = '.commands '
 if text.startswith(cm):
  text = text[len(cm):]
  cmds = text.split(u';')
  return [(typ, source, cmd, stanza) for cmd in cmds if cmd]

#class my_wrapper:
 #def __init__(self, item, typ):
  #self.item = item
  #self.typ = typ
 #def __getattribute__(self, name):
  #if name == 'lmsg': return self.lmsg
  #elif name == 'msg': return self.msg
  #else: return self.item.__getattribute__(name)
 #def msg(self, typ, body):
  #if self.typ == 'private': self.item.msg('chat', body)
  #elif self.typ == 'null': pass
 #def lmsg(self, typ, body):
  #if self.typ == 'private': self.item.lmsg('chat', body)
  #elif self.typ == 'null': pass

def null_handler(q):
 typ, source, text, stanza = q
 cm = '.null '
 if text.startswith(cm):
  text = text[len(cm):]
  #item = my_wrapper(source, 'null')
  return [('null', source, text, stanza)]

def private_handler(q):
 typ, source, text, stanza = q
 cm = '.private '
 if text.startswith(cm):
  text = text[len(cm):]
  return [('chat', source, text, stanza)]

def mynick_handler(q):
 typ, source, text, stanza = q
 if not source.room or not source.room.bot: return False
 cm = u'%s: ' % (source.room.bot.nick, )
 if text.startswith(cm):
  text = text[len(cm):]
  return [(typ, source, text, stanza)]

bot.register_rewrite_engine(commands_handler)
bot.register_rewrite_engine(null_handler)
bot.register_rewrite_engine(private_handler)
bot.register_rewrite_engine(mynick_handler)

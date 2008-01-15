import twisted
import twisted.python.log
from twisted.internet import reactor
from twisted.web.html import escape
from twisted.words.xish import domish
from item import item as new_item
from twistedwrapper import wrapper
from pluginloader import pluginloader
from muc import muc
import config
if config.ENABLE_SQLITE: import db
import time
import os
import sys
import lang
import log
import traceback
from cerberus import censor

class freqbot:

 def __init__(self, q):
  self.log = log.logger()
  if not os.access(config.LOGF, 0):
   fp = file(config.LOGF, 'w')
   fp.write('# freQ log\n')
   fp.close()
  twisted.python.log.startLogging(open(config.LOGF, 'a'))
  twisted.python.log.addObserver(self.error_handler)
  self.censor = censor()
  self.g = {}
  self.cmdhandlers = []
  self.msghandlers = []
  self.joinhandlers = []
  self.leavehandlers = []
  self.badhandlers = []
  self.version_name = u'freQ'
  self.version_version = u'1.0.99.' + self.getRev()
  self.version_os = u'Twisted %s, Python %s' % (twisted.__version__, sys.version)
  self.authd = 0
  self.wrapper = wrapper()
  self.wrapper.onauthd = self.onauthd
  self.wrapper.c.addBootstrap('//event/client/basicauth/authfailed', self.failed)
  self.wrapper.c.addBootstrap('//event/client/basicauth/invaliduser', self.failed)
  self.wrapper.register_handler(self.iq_handler, 'iq', 'get')
  self.wrapper.register_msg_handler(self.call_cmd_handlers)
  self.wrapper.register_msg_handler(self.call_msg_handlers)
  if config.ENABLE_SQLITE: self.db = db.db()
  self.alias_engine = None
  self.plug = pluginloader(self, q)
  print 'Initialized'
  self.log.log('<b>freQ %s (PID: %s) Initialized</b>' % (self.version_version, os.getpid()))

 def check_text(self, source, text):
  #if source.room and (source.room.bot.nick == self.muc.get_nick(source.room.jid)):
  # return #ignore own messages/presences
  if not text: return #ignore empty messages/statuses
  self.log.log(u'checking %s (from %s)' % (escape(text), escape(source.jid)), 1)
  bad_word = self.censor.respond(text)
  if bad_word:
   self.log.log(u'found bad word &lt;%s&gt;, let\'s call bad_handlers!' % (escape(bad_word), ), 3)
   self.call_bad_handlers(source, text, bad_word)
  else: self.log.log(u'bad words not found (result: %s)' % (bad_word, ), 1)

 def error_handler(self, m):
  try:
   if m['isError'] == 1:
    self.log.err(escape(repr(m)))
    reactor.stop()
   else:
    self.log.log(escape(repr(m)))
  except: print m 

 def failed(self, x):
  print 'connect failed!'
  self.log.err('cannot login to jabber account (eg invalid username/password ) :(')
  reactor.stop()

 def register_cmd_handler(self, func, cmd, required_access = 0, g = None):
  self.cmdhandlers.append((func, cmd, required_access, g))

 def register_msg_handler(self, func, g = None):
  self.msghandlers.append((func, g))

 def register_join_handler(self, func):
  self.joinhandlers.append(func)

 def register_bad_handler(self, func):
  self.badhandlers.append(func)

 def register_leave_handler(self, func):
  self.leavehandlers.append(func)

 def call_cmd_handlers(self, t, s, body, stanza):
  groupchat = s.split('/')[0]
  b = self.alias_engine(groupchat, body)
  params = b.split()
  nick = s[len(groupchat)+1:]
  try: item = self.g[groupchat][nick]
  except:
   item = new_item(self)
   item.jid = s
   item.realjid = s
  if item.room and (item.nick == self.muc.get_nick(item.room.jid)):
   self.log.log(u'own message from %s ignored' % (item.jid, ), 2)
   return #ignore own messages
  if len(params):
   cmd = b.split()[0]
   params = b[len(cmd)+1:]
   for i in self.cmdhandlers:
    if cmd.lower() == i[1]:
     if item.allowed(i[2]):
      if (item.room and item.room.bot) or not i[3]:
       self.log.log(u'Calling command handler <b>%s</b> for message <font color=red>%s</font> from <font color=blue>%s</font><br/>stanza: <font color=grey>%s</font>'
       		 % (escape(repr(i[0])), escape(b), s, escape(stanza.toXml())), 4)
       try: i[0](t, item, params)
       except:
	m = "".join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
	self.log.err(escape(m))
	item.msg(t, 'ERROR')
      else: item.lmsg(t, 'muc_only')
     else: item.lmsg(t, 'not_allowed')
  if item.room and (t == 'groupchat'): self.check_text(item, body) 

 def call_msg_handlers(self, t, s, b, stanza):
  for i in self.msghandlers:
    if (t == 'groupchat') or not i[1]: i[0](t, s, b)

 def call_bad_handlers(self, s, text, badword):
  for i in self.badhandlers: i(s, text, badword)

 def call_join_handlers(self, item):
  for i in self.joinhandlers:
   self.log.log('call_join_handler: %s' % (escape(repr(i)), ), 1)
   i(item)

 def call_leave_handlers(self, item, typ, reason):
  for i in self.leavehandlers:
   i(item, typ, reason)
   self.log.log('called_leave_handler(reason=%s,typ=%s): %s' % (reason, typ, escape(repr(i))), 1)
  # typ: 0: leave
  #      1: kick
  #      2: ban
  #      3: rename

 def onauthd(self):
  self.log.log('onauthd: stage 1')
  self.authd += 1
  if self.authd > config.RECONNECT_COUNT:
   self.log.err('RECONNECT limit exceeded...')
   reactor.stop()
  self.muc = muc(self)
  reactor.callLater(5, self.onauthd2)

 def onauthd2(self):
  self.log.log('onauthd: stage 2')
  groupchats = self.muc.load_groupchats()
  for i in groupchats: self.muc.join(i)
  print 'Joined %s groupchats' % len(groupchats, )

 def read_file(self, fn):
  f = file(fn, 'r')
  content = f.read().decode('utf8')
  r = f.close()
  return content

 def iq_handler(self, x):
  for child in x.children:
   if (child.__class__==domish.Element) and (child.name=='query') and (child.uri=='jabber:iq:version'):
    answer = domish.Element(('jabber:client', 'iq'))
    answer['type'] = 'result'
    answer['id'] = x.getAttribute('id')
    answer['to'] = x.getAttribute('from')
    query = answer.addElement('query', 'jabber:iq:version')
    query.addElement('name').addContent(self.version_name)
    query.addElement('version').addContent(self.version_version)
    query.addElement('os').addContent(self.version_os)
    self.wrapper.send(answer)

 def getRev(self):
  try:
   p = os.popen(config.SVNVERSION)
   time.sleep(1)
   return p.read()
  except: return 'dev' 

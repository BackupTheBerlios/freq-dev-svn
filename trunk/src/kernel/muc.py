#!/usr/bin/env python
# -*- coding: utf8 -*-
#~#######################################################################
#~ Copyright (c) 2008 Burdakov Daniel <kreved@kreved.org>               #
#~                                                                      #
#~ This file is part of FreQ-bot.                                       #
#~                                                                      #
#~ FreQ-bot is free software: you can redistribute it and/or modify     #
#~ it under the terms of the GNU General Public License as published by #
#~ the Free Software Foundation, either version 3 of the License, or    #
#~ (at your option) any later version.                                  #
#~                                                                      #
#~ FreQ-bot is distributed in the hope that it will be useful,          #
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#~ GNU General Public License for more details.                         #
#~                                                                      #
#~ You should have received a copy of the GNU General Public License    #
#~ along with FreQ-bot.  If not, see <http://www.gnu.org/licenses/>.    #
#~#######################################################################
from twisted.words.xish import domish
from twisted.web.html import escape
from item import item as new_item
from room import room as new_room
import config
import lang
import sys
import options

msglimit = 8000

class muc:

 def __init__(self, bot):
  self.g_file = '%s/text/groupchats.txt' % (config.DATADIR, )
  self.bot = bot
  self.join_handlers = []
  self.leave_handlers = []
  self.bot.wrapper.x.addObserver('/presence', self.presence_handler)
  self.bot.g = {}

 def msg(self, t, s, b):
  if len(b)>msglimit: b = b[:msglimit]+'... (truncated)'
  self.bot.log.log(escape(u'attempt to send message to %s (type "%s", body: %s)' % (s, t, b)), 3)
  if (s in self.bot.g.keys()) or (t=='chat'):
   if b == '': b = '[empty message]'
   self.bot.wrapper.msg(t, s, b)
  else:
   s = s.split('/')
   groupchat = s[0]
   nick = '/'.join(s[1:])
   self.bot.log.log(escape(u'send message to %s (type "%s", body: %s)' % (groupchat, t, b)), 3)
   self.bot.wrapper.msg(t, groupchat, '%s: %s' % (nick, b))

 def is_admin(self, jid):
  return jid and (jid.split('/')[0].lower() in config.ADMINS)

 def get_access(self, item):
  self.bot.log.log(u'checking access for %s (%s)...' % (item.jid, item.realjid), 1)
  access = 0
  if item.role == 'participant': access += 1
  if item.role == 'moderator': access +=4
  if item.affiliation == 'none': access += 1
  if item.affiliation == 'member': access +=3
  if item.affiliation == 'admin': access += 5
  if item.affiliation == 'owner': access += 7
  if self.is_admin(item.realjid):
   access += 50
   if item.room and (item.room.server() in config.TRUSTED_SERVERS):
    access += 50
  if self.is_admin(item.jid): access += 100
  for m in self.bot.access_modificators: access = m(item, access)
  return access

 def allowed(self, s, required_access):
  return self.get_access(s) >= required_access

 def invalid_syntax(self, t, s, text):
  try:
   s.lmsg(t, 'invalid_syntax', self.bot.read_file('doc/syntax/%s.txt' % (text, )).strip())
  except: s.lmsg(t, 'invalid_syntax_default')

 def presence_handler(self, x):
  if self.bot.stopped: return
  self.bot.log.log(u'presence_handler..', 1)
  try: typ = x['type']
  except: typ = 'available'
  jid = x['from'].split('/')
  groupchat = jid[0]
  nick = x['from'][len(groupchat)+1:]
  groupchat = self.bot.g.get(groupchat)
  if groupchat:
   if typ == 'available':
    item = groupchat.setdefault(nick, new_item(self.bot, groupchat))
    item.jid = x['from']
    try: item.status = [i for i in x.children if i.name=='status'][0].children[0]
    except: item.status = ''
    try: item.show = [i for i in x.children if i.name=='show'][0].children[0]
    except: item.show = 'online'
    item.nick = nick
    try:
     _x = [i for i in x.children if (i.name=='x') and (i.uri=='http://jabber.org/protocol/muc#user')][0]
     _item = [i for i in _x.children if i.name=='item'][0]
     item.affiliation = _item['affiliation']
     item.role = _item['role']
     try: item.realjid = _item['jid'].split('/')[0]
     except: item.realjid = item.jid
    except:
     self.bot.log.err(u"Got invalid presence from '%s'?\n%s: %s<br/><font color=grey>%s</font>" % (x['from'], escape(repr(sys.exc_info()[0])), escape(repr(sys.exc_info()[1])), escape(x.toXml())))
    if not item.handled:
     if item.nick == self.get_nick(groupchat.jid): # if item is bot...
      groupchat.bot = item
      gj = groupchat.joiner
      if gj:
       gj[0].lmsg(gj[1], 'join_success', groupchat.jid, nick)
       self.bot.log.log(u'reporting to %s about successful joining..' % (gj[0].jid, ), 6)
       groupchat.joiner = None
     item.handled = True
     self.call_join_handlers(item)
     self.bot.call_join_handlers(item)
    if not(item.nick == self.get_nick(groupchat.jid)): #if item isn't bot...
     self.bot.check_text(item, item.nick)
     self.bot.check_text(item, item.status)
   else:
    item = groupchat.pop(nick, None)
    if item:
     self.call_leave_handlers(item)
     # parse leave_type, reason
     # typ: 0: leave
     #      1: kick
     #      2: ban
     #      3: rename
     if typ == 'unavailable':
      #unavailable
      try:
       _x = [i for i in x.children if (i.name=='x') and (i.uri == 'http://jabber.org/protocol/muc#user')][0]
       _item = [i for i in _x.children if i.name=='item'][0]
       _status = [i['code'] for i in _x.children if i.name=='status']
       try: reason = [i for i in _item.children if i.name=='reason'][0].children[0]
       except: reason = ''
       try: new_nick = _item['nick']
       except: new_nick = '[unknown nick]'
       if '303' in _status: leave_type = 3
       else:
        if '301' in _status: leave_type = 2
        else:
         if '307' in _status: leave_type = 1
         else: leave_type = 0
      except:
       self.bot.log.err(u"Got invalid presence from '%s'?\n%s: %s<br/><font color=grey>%s</font>" % (x['from'], escape(repr(sys.exc_info()[0])), escape(repr(sys.exc_info()[1])), escape(x.toXml())))
       leave_type = 0
       reason = ''
      if leave_type == 3: #if item changes nickname
       reason = item.nick
       item.jid = u'%s/%s' % (groupchat.jid, new_nick)
       item.nick = new_nick
       groupchat[new_nick] = item
      self.bot.call_leave_handlers(item, leave_type, reason)
      if (item.nick == self.get_nick(groupchat.jid)) and (leave_type <> 3): self.leave(groupchat.jid)
     else:
      #error
      self.bot.log.err(u'unknown error presence: '+escape(x.toXml()))
    else:
     #if (nick == self.get_nick(groupchat.jid)): self.leave(groupchat.jid, 'error')
     #self.bot.log.err("'unavailable|error' presence from %s, but %s not in groupchatmap" % (x['from'], x['from']))
     #if nick == self.get_nick(groupchat.jid): self.leave(groupchat.jid, 'non-available presence')
     self.bot.log.err(u'unavailable|error from %s\nstanza:\n%s' % (escape(x['from']), escape(x.toXml())))
     gj = groupchat.joiner
     if gj:
      self.bot.log.log(u'reporting to %s about failed joining..' % (escape(gj[0].jid), ), 6)
      gj[0].lmsg(gj[1], 'join_failed', groupchat.jid, nick, x.toXml())
      groupchat.joiner = None
     if x['from'].endswith(self.get_nick(groupchat.jid)):
      self.bot.log.log(u'leave (unavailable|error) from %s\nstanza:\n%s' % (escape(x['from']), escape(x.toXml())), 7)
      self.leave(groupchat.jid, 'error|unavailable presence...')
  else:
   if typ in ('subscribe', 'subscribed', 'unsubscribe', 'unsubscribed'):
    p = domish.Element(('jabber:client', 'presence'))
    p['type'] = typ
    p['to'] = x['from']
    self.bot.wrapper.send(p)
    self.bot.log.log('ROSTER: %s - %s' % (typ, p['to']), 5)

 def register_join_handler(self, func):
  self.join_handlers.append(func)

 def register_leave_handler(self, func):
  self.leave_handlers.append(func)

 def call_join_handlers(self, item):
  if item.room.bot:
   for i in self.join_handlers: i(item)

 def call_leave_handlers(self, item):
  for i in self.leave_handlers: i(item)

 def get_nick(self, groupchat):
  return options.get_option(groupchat, 'nick', config.NICK)

 def set_nick(self, groupchat, nick):
  options.set_option(groupchat, 'nick', nick)

 def join(self, groupchat, nick=None):
  if nick == None: nick = self.get_nick(groupchat)
  else: self.set_nick(groupchat, nick)
  groupchat = groupchat.replace('\n', '')
  groupchat = self.bot.g.setdefault(groupchat, new_room(self.bot, groupchat))
  p = domish.Element(('jabber:client', 'presence'))
  p['to'] = u'%s/%s' % (groupchat.jid, nick)
  p.addElement('status').addContent(options.get_option(groupchat.jid, 'status', \
  config.STATUS.replace('%VERSION%', self.bot.version_version)))
  p.addElement('x', 'http://jabber.org/protocol/muc').addElement('history').__setitem__('maxchars', '0')
  self.bot.wrapper.send(p)
  q = self.load_groupchats()
  if not (groupchat.jid in q): self.dump_groupchats(q+[groupchat.jid])
  return groupchat

 def leave(self, groupchat, reason = 'leave'):
  p = domish.Element(('jabber:client', 'presence'))
  p['to'] = u'%s/%s' % (groupchat, self.get_nick(groupchat))
  p['type'] = 'unavailable'
  p.addElement('status').addContent(reason)
  self.bot.wrapper.send(p)
  q = self.load_groupchats()
  if groupchat in q:
   q.remove(groupchat)
   self.dump_groupchats(q)
  self.bot.g.pop(groupchat, None)

 def load_groupchats(self):
  try:
   f = file(self.g_file, 'r')
   g = f.read().decode('utf8').split(u'\n')
   f.close()
  except: g = []
  return [i.strip() for i in g if i]

 def dump_groupchats(self, groupchats):
  f = file(self.g_file, 'w')
  f.write(u'\n'.join(groupchats).encode('utf8'))
  f.close()

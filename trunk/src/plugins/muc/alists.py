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

import re
bigtime = 2000000000

class NickNotFound(Exception):
 def __init__(self, value):
  self.value = value
 def __str__(self):
  return repr(self.value)

class NoJID(Exception):
 def __init__(self, value):
  self.value = value
 def __str__(self):
  return repr(self.value)

class MyRegexpError(Exception):
 def __init__(self, value):
  self.value = value
 def __str__(self):
  return repr(self.value)

def parse_time(s):
 l = s[len(s)-1].lower()
 c = int(s[:len(s)-1])
 if l == 'd': return 86400 * c
 elif l == 'h': return 3600 * c
 elif l == 'm': return 60 * c
 elif l == 's': return c
 else: raise ValueError

class aitem:
 def __init__(self, room, s):
  """парсит выражения типа 'jid blabla@server', 'nick exp regexp', etc.
  короче в стиле глюкса"""
  self.room = room
  if s.startswith('/'):
   n = s.find(' ')
   self.end_time = int(parse_time(s[1:n]) + time.time())
   s = s[n+1:]
  elif s.startswith('@#/'):
   n = s.find(' ')
   self.end_time = int(s[3:n])
   s = s[n+1:]
  else: self.end_time = bigtime
  s = s.strip().lower()
  if s.startswith('jid '):
   self.by_jid = True
   s = s[4:]
   if not s: raise ValueError
  elif s.startswith('nick '):
   self.by_jid = False
   s = s[5:]
   if not s: raise ValueError
  else:
   self.by_jid = True
   self.regexp = False
   item = room.get(s, None)
   if item:
    if item.jid == item.realjid: raise NoJID(item.jid)
    else: self.value = item.realjid
   else: raise NickNotFound(s)
   return
  if s.startswith('exp '):
   self.regexp = True
   s = s[4:]
   try: re.match(s, 'test@jabber.org')
   except: raise MyRegexpError(s)
  else: self.regexp = False
  self.value = s
 def text(self, human = False):
  if self.by_jid: text = 'jid '
  else: text = 'nick '
  if self.regexp: text = text + u'exp '
  text = text + self.value
  if self.end_time < bigtime:
   if human: return u'%s (%s %s)' % (text, self.room.get_msg('alist_left'), time2str(self.end_time - time.time(), True, self.room.get_lang()))
   else: return u'@#/%d %s' % (self.end_time, text)
  else: return text
 def describe(self):
  return u'aitem: "%s", regexp: %s, by_jid: %s, value="%s"' % \
  (self.text(True), self.regexp, self.by_jid, self.value)
 def check(self, item):
  if self.by_jid: s = item.realjid
  else: s = item.nick
  if self.regexp: return re.match(self.value, s)
  else: return (self.value == s)

class alist:
 def __init__(self, bot, typ, action):
  self.action = action
  self.lists = optstringlist(typ)
  bot.register_join_handler(self.join_handler)
  bot.register_leave_handler(self.leave_handler)
 def append(self, room, s):
  q = aitem(room, s).text()
  p = self.lists[room.jid]
  p.append(q)
  p.sort()
  self.lists[room.jid] = p
  self.apply_to_room(room)
 def delete(self, room, n):
  p = self.lists[room.jid]
  p.pop(n-1)
  self.lists[room.jid] = p
 def items(self, room):
  q = [aitem(room, i) for i in self.lists[room.jid]]
  t = time.time()
  if [True for i in q if i.end_time<t]:
   q = [i for i in q if i.end_time>t]
   self.lists[room.jid] = [i.text() for i in q]
  return q
 def clear(self, room):
  self.lists[room.jid] = []
 def check(self, room, item):
  q = [True for i in self.items(room) if i.check(item)]
  return (len(q) > 0)
 def cmd(self, typ, source, cmd):
  room = source.room
  if cmd.count(' '):
   n = cmd.find(' ')
   c, p = cmd[:n], cmd[n+1:]
  else: c, p = cmd, ''
  if c == 'del':
   try: n = int(p)
   except:
    source.lmsg(typ, 'invalid_syntax_default')
    return
   if len(self.items(room)) < n: source.lmsg(typ, 'number_not_found')
   else:
    self.delete(room, n)
    source.lmsg(typ, 'deleted')
  elif c in ['list', 'show']:
   q = [i.text(True) for i in self.items(room)]
   if q: source.msg(typ, show_list(q, p, source.get_msg('not_found')))
   else: source.lmsg(typ, 'list_empty')
  elif c == 'clear':
   self.clear(room)
   source.lmsg(typ, 'cleared')
  else:
   try: self.append(room, cmd)
   except NickNotFound: source.lmsg(typ, 'nick_not_found')
   except NoJID: source.lmsg(typ, 'alist_add_nojid')
   except MyRegexpError: source.lmsg(typ, 'invalid_regexp')
   except ValueError: source.lmsg(typ, 'invalid_syntax_default')
   source.lmsg(typ, 'added')
 def apply_to_item(self, item):
  if self.check(item.room, item): self.action(item)
 def apply_to_room(self, room):
  for nick in room.keys(): self.apply_to_item(room[nick])
 def join_handler(self, item):
  self.apply_to_item(item)
 def leave_handler(self, item, typ, reason):
  if typ == 3: #changed nick
   self.apply_to_item(item)

def a_kick(item):
 item.room.moderate('nick', item.nick, 'role', 'none', 'akick')

def a_visitor(item):
 item.room.moderate('nick', item.nick, 'role', 'visitor', '')

def a_moderator(item):
 item.room.moderate('nick', item.nick, 'role', 'moderator', '')

AKICK = alist(bot, 'akick', a_kick)
AMODERATOR = alist(bot, 'amoderator', a_moderator)
AVISITOR = alist(bot, 'avisitor', a_visitor)

def akick_handler(t, s, p):
 p = p.strip().lower()
 if not p: s.syntax(t, 'akick')
 else: AKICK.cmd(t, s, p)

def avisitor_handler(t, s, p):
 p = p.strip().lower()
 if not p: s.syntax(t, 'avisitor')
 else: AVISITOR.cmd(t, s, p)

def amoderator_handler(t, s, p):
 p = p.strip().lower()
 if not p: s.syntax(t, 'amoderator')
 else: AMODERATOR.cmd(t, s, p)

bot.register_cmd_handler(akick_handler, '.akick', 9, True)
bot.register_cmd_handler(avisitor_handler, '.avisitor', 9, True)
bot.register_cmd_handler(amoderator_handler, '.amoderator', 9, True)

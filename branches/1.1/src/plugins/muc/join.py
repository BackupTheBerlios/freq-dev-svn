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

def join_handler(t, s, p):
 p = p.replace('\n', '')
 if p.count('/'): s.lmsg(t, 'join_slash')
 else:
  if not p: s.syntax(t, 'join')
  else:
   if p.count(' '):
    groupchat = p.split()[0]
    nick = p[len(groupchat)+1:]
   else:
    groupchat = p
    nick = config.NICK
   if groupchat in bot.g.keys(): s.lmsg(t, 'join_already_there')
   else:
    q = blacklist_load()
    if groupchat in q.keys():
     tm, reason = q[groupchat]
     if reason: m = s.get_msg('join_not_permitted_reason', (groupchat, reason))
     else: m = s.get_msg('join_not_permitted', (groupchat, ))
     m = dump_time(tm, m, True, s)
     s.msg(t, m)
    else:
     g = bot.muc.join(groupchat, nick)
     g.joiner = (s, t)
     bot.log.log_e(u'joining %s (asked by %s)' % (p, s.jid), 5)

bot.register_cmd_handler(join_handler, '.join', config.JOIN_ACCESS)

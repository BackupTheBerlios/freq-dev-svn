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
def uptime_handler(t, s, p):
 if p:
  packet = IQ(bot.wrapper.x, 'get')
  packet.addElement('query', 'jabber:iq:last')
  packet.addCallback(uptime_result_handler, t, s, p)
  reactor.callFromThread(packet.send, p)
 else: s.syntax(t, 'uptime')

def uptime_result_handler(t, s, p, x):
 try:
  s.lmsg(t, 'uptime_result', p, time2str(int(x.children[0]['seconds']), 1, lang.getLang(s.jid)))
 except:
  s.lmsg(t, 'uptime_error')
  #raise

bot.register_cmd_handler(uptime_handler, '.uptime')


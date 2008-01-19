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
def context_replace(text, t, s):
 text = text.replace(r'%NICK%', s.nick).replace(r'%JID%', s.realjid).replace(r'%ROLE%', s.role).replace(r'%AFFILIATION%', s.affiliation)
 if s.room: text = text.replace(r'%ROOM%', s.room.jid).replace(r'%SUBJECT%', TOPICS.get(s.room.jid, '[empty]'))
 if s.room and s.room.bot: text = text.replace(r'%BOT%', s.room.bot.nick)
 return text

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
def groupchats_handler(t, s, p):
 q = bot.g.keys()
 q.sort(lambda x, y: len(bot.g[y].items)-len(bot.g[x].items))
 q = ['%s(%s)' % (g, bot.g[g].count()) for g in q]
 q = [i.replace(config.DEFAULT_MUC_SERVER, '') for i in q]
 s.lmsg(t, 'groupchats', u', '.join(q), len(q))

bot.register_cmd_handler(groupchats_handler, '.groupchats')

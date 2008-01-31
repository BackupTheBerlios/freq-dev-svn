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
import os
import sys

class pluginloader:
 def __init__(self, bot, q):
  self.bot = bot
  self.q = q
  self.pluginlist = os.listdir('src/plugins');
 def load_all(self):
  sys.stdout.write('Loading plugins')
  for i in self.pluginlist:
   self.load(i)
   sys.stdout.write('.')
  print ' ok'
 def load(self, p):
  tl = os.listdir('src/plugins/'+p)
  tl = [i for i in tl if i.endswith('.py')]
  for i in tl:
   fn = 'src/plugins/%s/%s' % (p, i);
   fp = file(fn, 'r')
   pc = fp.read()
   fp.close()
   try:
    exec pc in self.q
   except:
    sys.stderr.write('\nCan\'t load plugin %s:\n' % (fn, ))
    raise


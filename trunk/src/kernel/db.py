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
import log
from pysqlite2 import dbapi2 as sqlite
import time
import random
from config import DATADIR

class db:
 def __init__(self):
  self.cache={}
  self.dbdir='%s/db' % (DATADIR, )
 def set(self, n, r, p, now=None):
  self.cache[n]=self.cache.get(n, [])
  self.cache[n].append((r, p))
  if now:
   c=sqlite.connect('%s/%s.db' % (self.dbdir, n))
   cur=c.cursor()
   while self.cache[n]:
    q=self.cache[n].pop(0)
    cur.execute(q[0], q[1])
   c.commit()
   c.close()
 def get(self, n, r, p):
  c=sqlite.connect('%s/%s.db' % (self.dbdir, n))
  cur=c.cursor()
  self.cache[n]=self.cache.get(n, [])
  while self.cache[n]:
   q=self.cache[n].pop(0)
   cur.execute(q[0], q[1])
  c.commit()
  cur.execute(r, p)
  p=cur.fetchall()
  c.commit()
  c.close()
  return p


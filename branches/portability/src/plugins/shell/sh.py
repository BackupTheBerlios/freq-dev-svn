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

def sh_handler(t, s, p):
 pipe = os.popen('sh -c "%s" 2>&1' % (p.encode('utf8', 'replace'), ))
 time.sleep(1)
 m = clear_text(pipe.read().decode('utf8', 'replace'))
 s.msg(t, m)

bot.register_cmd_handler(sh_handler, '.sh', 100)

svn_regexp = re.compile(u'^((https?|svn)\:\/\/)?(((\w|\-)+\.)+\w+)(\/(\w|\-)+)*\/?$')

def svn_handler(t, s, p):
 p = p.strip()
 if svn_regexp.match(p):
  pipe = os.popen('sh -c "svn log %s --limit 1" 2>&1' % (p.encode('utf8', 'replace'), ))
  time.sleep(1)
  m = clear_text(pipe.read().decode('utf8', 'replace'))
  ml = m.splitlines()
  m = '\n'.join(line for line in ml if not line.startswith('-----'))
  s.msg(t, m)
 else: s.syntax(t, 'svn')

bot.register_cmd_handler(svn_handler, '.svn')

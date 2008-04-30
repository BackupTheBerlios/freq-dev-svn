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
import google
google.setLicense(config.GOOGLE_KEY)

G_CACHE = {} # google search history (for .google next)

def google_handler(t, s, p):
 p = re.search('^(((([0-9]{1,5})(\-([0-9]{1,5}))?)|next))?(\ ?.+)?$', p)
 if p: p = p.groups()
 else:
  s.syntax(t, 'google')
  return
 n = p[1]
 start = p[3]
 if start == '0': start =1
 finish = p[5]
 q = p[6]
 if n == 'next':
  if G_CACHE.has_key(s.jid):
   start, finish, q = G_CACHE[s.jid]
   d = finish-start+1
   start, finish = start+d, finish+d
  else:
   s.lmsg(t, 'google_history_notfound')
   return
 if not start: start = '1'
 if not finish: finish = start
 if not q:
  s.lmsg(t, 'google?')
  return
 G_CACHE[s.jid] = (int(start), int(finish), q)
 #s.msg(t, u'%s: %s-%s' % (q, start, finish))
 try:
  x = google.doGoogleSearch(q, start=int(start)-1, maxResults=min(int(finish)-int(start)+1, 10), filter=1)
  if x.results:
   s.lmsg(t, 'google_results', show_list([lang.msg('google_result', (htmldecode(i.snippet), i.URL, i.cachedSize), lang.getLang(s.jid)) for i in x.results]), x.meta.estimatedTotalResultsCount)
  else: s.lmsg(t, 'google_no_results')
 except:
  s.lmsg(t, 'google_error')

bot.register_cmd_handler(google_handler, '.google')

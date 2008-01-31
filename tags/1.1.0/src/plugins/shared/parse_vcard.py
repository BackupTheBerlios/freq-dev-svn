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

VCARD_FIELDS = { 
'ru::FN'       : u'Полное имя', 
'ru::URL'      : u'Сайт',
'ru::BDAY'     : u'День рождения',
'ru::DESC'     : u'О себе',
'en::FN'       : u'Full Name',
'en::URL'      : u'Homepage',
'en::BDAY'     : u'Birthday',
'en::DESC'     : u'About'
}

def vcard_describe(field, lang):
 field = field[:len(field)-1]
 m = lang + '::' + field
 if m in VCARD_FIELDS.keys(): return VCARD_FIELDS[m]
 else: return field

def parse_vcard(x):
 r = {}
 if x.children:
  if x.children[0].__class__ == domish.Element: 
   for i in x.children:
    q = parse_vcard(i)
    for j in q.keys():
     r['%s/%s' % (i.name, j)] = q[j]
  else:
   return {'': x.children[0]}
 else: return {}
 return r


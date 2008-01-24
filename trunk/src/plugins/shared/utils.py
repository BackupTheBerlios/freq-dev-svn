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

# .test 'abc\\\\'d'

def my_quote(text):
 return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'

def my_replace(text, s1, s2):
 if text.count(s1):
  n = text.index(s1)
  return text[:n] + s2 + my_replace(text[n+len(s1):], s1, s2)
 else: return text

def get_end_count(text, d, n):
 if text.endswith(d): return get_end_count(text[:len(text)-1], d, n+1)
 else: return n

def get_param(text):
 text = text.strip()
 if not text: return ('', '')
 if text[0] in ["'", '"']:
  d = text[0]
  text = text[1:]
  if text.count(d):
   n = text.find(d)
   if (n > 0) and (text[n-1] == '\\'):
    p = text[:n-1]
    text = text[n:].strip()
    q = get_end_count(p, '\\', 0)
    print (p, text, q)
    if q % 2 == 1:
     p = my_replace(p, '\\\\', '\\')
     text = text[1:].strip()
    else:
     p = my_replace(p, '\\\\', '\\')
     a, b = get_param(text)
     p, text = p + d + a, b
   else:
    p, text = my_replace(text[:n], '\\\\', '\\'), text[n+1:].strip()
  else: raise ValueError('unbalanced quotes')
 else:
  if text.count(' '):
   n = text.find(' ')
   p = text[:n]
   text = text[n:].strip()
  else: p, text = text, ''
 return (p, text)

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
import sys
import os
import re
from twisted.web.html import escape

help = sys.argv[1]
html = sys.argv[2]
tpl = sys.argv[3]
vvv = sys.argv[4]

def use_tpl(fn, lng, *params):
 t = open('%s/%s-%s.html' % (tpl, fn, lng), 'r').read()
 return t % params

def load_help_content(k, l):
 fn = u'%s/%s-%s.txt' % (help, k, l)
 try:
  fp = file(fn.encode('utf8'), 'r')
  ctg = fp.readline()
  content = escape(fp.read())
  fp.close()
 except: content = '[ not translated yet to language "%s" ]' % (l, )
 return content

HELP_LANGS = {}
HELP_CATEGORIES = {}
q = os.listdir(help)
for i in q:
 p = re.search(u'^\.*(.+)\-(..)\.txt$', i)
 if p:
  p = p.groups()
  language = p[1]
  p = p[0]
  HELP_LANGS.setdefault(p, [])
  HELP_LANGS[p].append(language)
  fn = '%s/%s' % (help, i)
  fp = file(fn, 'r')
  c = fp.readline()
  fp.close()
  for j in c.split():
   HELP_CATEGORIES.setdefault(j, [])
   if not p in HELP_CATEGORIES[j]: HELP_CATEGORIES[j].append(p)

def process(lng):
 print 'creating "%s" docs' % (lng, )
 os.mkdir('%s/%s' % (html, lng))
 idx = use_tpl('doc.idx.head', lng, vvv)
 for cat in HELP_CATEGORIES.keys():
  q = use_tpl('doc.ctg.head', lng, cat)
  idx = idx + use_tpl('doc.idx.ctg', lng, cat, cat)
  for cmd in HELP_CATEGORIES[cat]:
   q = q + use_tpl('doc.ctg.cmd', lng, cmd, load_help_content(cmd, lng))
  q = q + use_tpl('doc.ctg.foot', lng)
  fp = open('%s/%s/%s.html' % (html, lng, cat), 'w')
  fp.write(q);
  fp.close()
 idx = idx + use_tpl('doc.idx.foot', lng)
 fp = open('%s/%s/index.html' % (html, lng), 'w')
 fp.write(idx)
 fp.close()
 
process('en')
process('ru')
process('ua')

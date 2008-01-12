#!/usr/local/bin/python

print 'Initializing...'

import sys
from twisted.words.protocols.jabber import xmlstream
from twisted.words.protocols.jabber.client import IQ
from twisted.web.html import escape
import traceback
import re
from twisted.internet import reactor
import os
import time

wd = os.path.dirname(sys.argv[0])
if not wd: wd = '.'
os.chdir(wd)
sys.path.insert(0, 'src/kernel')
sys.path.insert(0, 'modules')
#print 'sys.path is %s' % (sys.path, )

import config
if len(sys.argv) > 1: cfg = sys.argv[1]
else: cfg = './freq.conf'
print 'Using %s as config file' % (cfg, )
config.init(cfg)
  
try:
 fp = file(config.PIDFILE, 'r')
 p = fp.read()
 fp.close()
 os.kill(int(p), 9)
 time.sleep(5)
 sys.stdout.write('pid %s killed.. ' % (p, ))
except: pass
fp = file(config.PIDFILE, 'w')
fp.write(str(os.getpid()))
fp.close()

from freq import freqbot
import lang

bot = freqbot(globals())
try:
 bot.plug.load_all()
 print 'reactor.run()'
 reactor.run()
except:
 bot.log.err(escape('FATAL ERROR: %s' % (traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback), )))
 del bot
 raise
 
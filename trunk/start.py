#!/usr/local/bin/python

from twisted.web.html import escape
import traceback
import re
import config
from twisted.internet import reactor
import sys
import os
import time
os.chdir(os.path.dirname(sys.argv[0]))
sys.path.insert(1, "src/kernel")
try:
 fp=file(config.PIDFILE, "r")
 p=fp.read()
 fp.close()
 os.kill(int(p), 9)
 time.sleep(5)
 print "pid %s killed." % (p, )
except: pass
fp=file(config.PIDFILE, "w")
fp.write(str(os.getpid()))
fp.close()

from freq import freqbot
import lang

try:
 bot=freqbot(globals())
 bot.plug.load_all()
 print "Plugins loaded. Starting"
 reactor.run()
except:
 bot.log.err(escape('fatal error: %s' % (traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback), )))
 # if restart...


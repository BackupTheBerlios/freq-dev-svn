#!/usr/local/bin/python

import sys
import os
import time
os.chdir(os.path.dirname(sys.argv[0]))
sys.path.insert(1, "src/kernel")
try:
 fp=file("freq.pid", "r")
 p=fp.read()
 fp.close()
 os.kill(int(p), 9)
 time.sleep(5)
 print "pid %s killed." % (p, )
except: pass
fp=file("freq.pid", "w")
fp.write(str(os.getpid()))
fp.close()

from freq import freqbot

bot=freqbot();
reactor.run()


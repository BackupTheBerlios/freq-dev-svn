#!/usr/local/bin/python

import sys
import os
import time
os.chdir(os.path.dirname(sys.argv[0]))
sys.path.insert(1, "src/kernel")
os.execv("kill `cat freq.pid`")
time.sleep(5)
fp=file("freq.pid", "w")
fp.write(str(os.getpid()))
fp.close()

from freq import freqbot

bot=freqbot();


import os
import time
import config
import lang

class logger:
 def __init__(self): pass
 def _log(self, fn, m, h):
  if not os.access(fn, 0):
   fp=file(fn, "w")
   fp.write(h)
   fp.close()
  fp=file(fn, "a")
  fp.write(m.encode("utf8"))
  fp.close()
 def log(self, m, level=9):
  if level>config.LOGLEVEL: self._log(config.LOGFILE, time.strftime(lang.get("log.record")) % (m, ), lang.get("log.header"))
 def err(self, m):
  self._log(config.ERRLOGFILE, time.strftime(lang.get("log.record")) % (m, ), lang.get("log.header"))


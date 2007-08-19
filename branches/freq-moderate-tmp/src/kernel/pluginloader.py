import os
import sys

class pluginloader:
 def __init__(self, bot, q):
  self.bot = bot
  self.q = q
  self.pluginlist = os.listdir("src/plugins");
 def load_all(self):
  sys.stdout.write('Loading plugins')
  for i in self.pluginlist:
   self.load(i)
   sys.stdout.write('.')
  print 'ok'
 def load(self, p):
  tl=os.listdir("src/plugins/"+p)
  tl=[i for i in tl if i.endswith(".py")]
  for i in tl:
   fn="src/plugins/%s/%s" % (p, i);
   fp=file(fn, "r")
   pc=fp.read()
   fp.close()
   exec pc in self.q


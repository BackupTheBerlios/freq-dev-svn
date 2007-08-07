import os
import sys

class pluginloader:
 def __init__(self, bot):
  self.bot=bot;
  self.pluginlist=os.listdir("src/plugins");
  self.pluginlist=[i for i in self.pluginlist if i.count("plugin")]
 def load_all(self):
  for i in self.pluginlist: self.load(i);
 def load(self, p):
  tl=os.listdir("src/plugins/"+p)
  for i in tl:
   fp=file("src/plugins/%s/%s" % (p, i), "r")
   pc=fp.read()
   fp.close()
   exec pc in globals();


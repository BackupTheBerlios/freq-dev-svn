import os
import sys

class pluginloader:
 def __init__(self, bot):
  self.bot=bot;
  self.pluginlist=os.listdir("src/plugins");
 def load_all(self):
  for i in self.pluginlist: self.load(i);
 def load(self, p):
  tl=os.listdir("src/plugins/"+p)
  for i in tl:
   fp=file(i, "r")
   pc=fp.read()
   fp.close()
   exec pc in globals();


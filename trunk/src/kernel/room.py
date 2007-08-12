import config
import options
from item import item as titem

class room:
 def __init__(self, bot, jid):
  self.bot = None
  self.globalbot = bot
  self.items = {}
  self.__getitem__ = self.items.__getitem__
  self.__setitem__ = self.items.__setitem__
  self.get = self.items.get
  self.has_key = self.items.has_key
  self.keys = self.items.keys
  self.jid = jid
  self.setdefault = self.items.setdefault
  self.pop = self.items.pop
 def get_option(self, k, d=None):
  return options.get_option(self.jid, k, d)
 def set_option(self, k, v):
  options.set_option(self.jid, k, v)
 def get_msglimit(self):
  return int(self.get_option('msglimit', config.MSGLIMIT))
 def set_msglimit(self, value):
  return self.set_option('msglimit', str(value))


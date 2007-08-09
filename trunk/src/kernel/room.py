from item import item as titem

class room:
 def __init__(self, bot, jid):
  self.bot=None
  self.globalbot=bot
  self.items={}
  self.__getitem__=self.items.__getitem__
  self.__setitem__=self.items.__setitem__
  self.get=self.items.get
  self.has_key=self.items.has_key
  self.keys=self.items.keys
  self.jid = jid
  self.setdefault = self.items.setdefault
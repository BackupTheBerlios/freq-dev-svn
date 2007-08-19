import config
import options
from twisted.internet.defer import Deferred
from twisted.words.protocols.jabber.client import IQ
from twisted.internet.reactor import callFromThread
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
 def rejoin(self):
  self.globalbot.muc.join(self.jid)
 def moderate(self, jn, jid_nick, ra, set_to, reason):
  packet = IQ(self.globalbot.wrapper.x, 'set')
  query = packet.addElement('query', 'http://jabber.org/protocol/muc#admin')
  query.addElement('reason').addContent(reason)
  i = query.addElement('item')
  i[jn] = jid_nick
  i[ra] = set_to
  d = Deferred()
  packet.addCallback(d.callback)
  callFromThread(packet.send, self.jid)
  return d


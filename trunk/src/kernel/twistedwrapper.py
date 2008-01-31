#!/usr/bin/env python
# -*- coding: utf8 -*-
#~#######################################################################
#~ Copyright (c) 2008 Burdakov Daniel <kreved@kreved.org>               #
#~                                                                      #
#~ This file is part of FreQ-bot.                                       #
#~                                                                      #
#~ FreQ-bot is free software: you can redistribute it and/or modify     #
#~ it under the terms of the GNU General Public License as published by #
#~ the Free Software Foundation, either version 3 of the License, or    #
#~ (at your option) any later version.                                  #
#~                                                                      #
#~ FreQ-bot is distributed in the hope that it will be useful,          #
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#~ GNU General Public License for more details.                         #
#~                                                                      #
#~ You should have received a copy of the GNU General Public License    #
#~ along with FreQ-bot.  If not, see <http://www.gnu.org/licenses/>.    #
#~#######################################################################

import twisted
from twisted.names.srvconnect import SRVConnector
from twisted.words.protocols.jabber import client, jid, xmlstream, sasl
from twisted.words.protocols.jabber.client import CheckVersionInitializer,BindInitializer,SessionInitializer
from twisted.words.protocols.jabber.sasl import SASLNoAcceptableMechanism,SASLAuthError,get_mechanisms,sasl_mechanisms
from twisted.words.xish import domish
from twisted.internet import reactor, threads, defer
from twisted.web.html import escape
import traceback
import re
import log
import sys
import config
import time

#here we use some code from J2J <http://jrudevels.org/>

class XMPPAndGoogleAuthenticator(client.XMPPAuthenticator):
    def __init__(self,jid,password,client):
        self.client = client
        twisted.words.protocols.jabber.client.XMPPAuthenticator.__init__(self,jid,password)

    def associateWithStream(self, xs):
        xmlstream.ConnectAuthenticator.associateWithStream(self, xs)

        xs.initializers = [CheckVersionInitializer(xs)]
        inits = [ (xmlstream.TLSInitiatingInitializer, False,False),
                  (SASLAndXGoogleToken, True,True),
                  (BindInitializer, False,False),
                  (SessionInitializer, False,False),
                ]

        for initClass, required, isGoogleClass in inits:
            if not isGoogleClass:
                init = initClass(xs)
            else:
                init = initClass(xs,self.client)
            init.required = required
            xs.initializers.append(init)

class SASLAndXGoogleToken(sasl.SASLInitiatingInitializer):
    def __init__(self,xs,client):
        self.client=client
        sasl.SASLInitiatingInitializer.__init__(self,xs)

    def start(self):
        jid = self.xmlstream.authenticator.jid
        password = self.xmlstream.authenticator.password

        mechanisms = get_mechanisms(self.xmlstream)

        if 'DIGEST-MD5' in mechanisms:
            self.mechanism = sasl_mechanisms.DigestMD5('xmpp', jid.host, None,
                                                       jid.user, password)
        elif 'PLAIN' in mechanisms:
            self.mechanism = sasl_mechanisms.Plain(None, jid.user, password)
        else:
            return defer.fail(SASLNoAcceptableMechanism)

        self._deferred = defer.Deferred()
        self.xmlstream.addObserver('/challenge', self.onChallenge)
        self.xmlstream.addOnetimeObserver('/success', self.onSuccess)
        self.xmlstream.addOnetimeObserver('/failure', self.onFailure)
        self.sendAuth(self.mechanism.getInitialResponse())
        return self._deferred

class XMPPClientConnector(SRVConnector):
    def __init__(self, reactor, domain, factory, port=5222):
        self.port=port
        SRVConnector.__init__(self, reactor, 'xmpp-client', domain, factory)

class ClientFactory(xmlstream.XmlStreamFactory):
    def __init__(self,a,host):
        self.host = host
        xmlstream.XmlStreamFactory.__init__(self,a)
        self.maxRetries = 0

    def clientConnectionFailed(self, connector, reason):
        self.host.log.err('connection failed!')
        self.host.log.log('connection failed!')
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        self.host.log.err('connection lost!')
        self.host.log.log('connection lost!')
        reactor.stop()

class wrapper:

 def __init__(self, version):
  #self.lastsent = {}
  #self.queues = {}
  self.version = version
  self.tc = 0
  self.th = {}
  self.sjid = u'%s@%s/%s' % (config.USER, config.SERVER, config.RESOURCE)
  self.jid = jid.JID(self.sjid)
  self.onauthd = None
  self.tryingSRV = True
  self.tryingNonSASL = False
  self.tryingSASL = True
  #self.c = client.basicClientFactory(self.jid, config.PASSWD)
  a = XMPPAndGoogleAuthenticator(self.jid, config.PASSWD, self)
  self.c = ClientFactory(a,self)
  self.c.maxRetries = 0
  self.c.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, self.authd)
  self.c.addBootstrap(xmlstream.INIT_FAILED_EVENT, self.initfailed)
  self.c.addBootstrap(xmlstream.STREAM_CONNECTED_EVENT, self.onConnected)
  self.c.addBootstrap(xmlstream.STREAM_END_EVENT, self.onDisconnected)
  self.x = None
  self.log = log.logger()
  self.handlers = []
  self.msghandlers = []
  #self.send_from_queue(True)
  #self.clean_queue()
  port = config.PORT
  server = config.CONNECT_SERVER
  if not server: server = config.SERVER
  self.connector = XMPPClientConnector(reactor, server, self.c, port)
  self.connector.connect()
  #reactor.connectTCP(server, port, self.c)

 def onConnected(self, xs):
  self.x = xs
  self.log.log('connected!')

 def presence(self, status=None):
  if not self.x: return
  if not status: status = config.STATUS.replace(r'%VERSION%', self.version)
  p = domish.Element(('jabber:client', 'presence'))
  p.addElement('status').addContent(status)
  p.addElement('show').addContent('chat')
  self.x.send(p)

 def getChild(self, x, n):
  return [i for i in x.children if (i.__class__==domish.Element) and (i.name==n)][0]

 def authd(self, x):
  self.log.log('Authenticated')
  #self.x.addObserver('/*', self.cb)
  self.x.addObserver('/message', self.cbmessage)
  self.onauthd()

 def initfailed(self, x):
  self.log.err('INIT_FAILED_EVENT')
  reactor.stop()

 def onDisconnected(self, x):
  self.log.err('Disconnect!')
  reactor.stop()

 def cb(self, x):
  n = x.name
  try: id = x['id']
  except: id = 'something'
  try: typ = x['type']
  except: typ = ''
  try: body = self.getChild(x, 'body').children[0]
  except: body = ''
  try: f = x['from']
  except: f = config.SERVER
  for i in self.handlers:
   if (i[0] in (n, None)) and (i[1] in (typ, None)) and (i[2] in (id, None)) and (i[3] in (body, None)) and (i[4] in (f, None)):
    if i[6]: self.handlers.remove(i)
    self.call(i[5], x)

 def register_handler(self, func, stanza=None, typ=None, id=None, body=None, f=None, once=None):
  self.handlers.append((stanza, typ, id, body, f, func, once))

 def register_msg_handler(self, func):
  self.msghandlers.append(func)

 def cbmessage(self, x):
  delayed = [i for i in x.children if (i.__class__==domish.Element) and ((i.name=='delay') or ((i.name=='x') and (i.uri=='jabber:x:delay')))]
  try: body = self.getChild(x, 'body').children[0]
  except: body = ''
  try: subject = self.getChild(x, 'subject').children[0]
  except: subject = None
  try: f = x['from']
  except: f = config.SERVER
  try: typ = x['type']
  except: typ = 'chat'
  #if typ == 'error':
   #self.log.err('got ERROR message stanza: <font color=grey>%s</font><br>something wrong?' % (escape(x.toXml()), ))
  if subject or not delayed:
   for i in self.msghandlers:
    self.call(i, typ, f, body, subject, x)

 def send(self, x):
  #ujid = jid.JID(x['to'])
  self.log.log(u'try to send stanza to %s..' % (x['to'], ), 0)
  reactor.callFromThread(self._send, x)
  #if {???}: #time.time()-self.lastsent.get(ujid.userhost(), 0)<config.QUEUE_SEND_INTERVAL:
   ##don't send, add it to queue
   #q = self.queues.setdefault(ujid.userhost(), [])
   #if len(q) > config.QUEUE_LIMIT:
    #self.log.err('WARNING: QUEUE overflow for jid=%s!' % (ujid.userhost(), ))
   #else:
    #q.append(x)
    #reactor.callFromThread(self.send_from_queue)
  #else:
   #send now
   #self.log.log(u'try to send stanza to %s.. STAGE 2 [immediately]' % (x['to'], ), 0)
   #reactor.callFromThread(self.x.send, x)
   #self.lastsent[ujid.userhost()] = time.time()

 #def send_from_queue(self, b=False):
  #for sjid in self.queues.keys():
   #if (time.time()-self.lastsent.get(sjid, 0)>config.QUEUE_SEND_INTERVAL) and (len(self.queues[sjid])>0):
    #x = self.queues[sjid].pop(0)
    #self.log.log(u'try to send stanza to %s.. STAGE 2 [from queue]' % (x['to'], ), 1)
    #self.lastsent[sjid] = time.time()
    #self.x.send(x)
  #if b: reactor.callLater(1, self.send_from_queue)

 #def clean_queue(self):
  #for sjid in self.lastsent.keys():
   #if time.time()-self.lastsent[sjid]>60: self.lastsent.pop(sjid)
  #for sjid in self.queues.keys():
   #if len(self.queues[sjid]) == 0: self.queues.pop(sjid)
  #self.log.log('twistedwrapper.clean_queue executed...', 2)
  #reactor.callLater(60, self.clean_queue)

 def _send(self, x):
  try: self.x.send(x)
  except:
   try: xml = x.toXml()
   except: xml = '[can\'t x.toXml()]'
   m = '; '.join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
   m = m.decode('utf8', 'replace')
   self.log.err_e('Can\'t send stanza! (xml: %s). Error: %s' % (xml, m))

 def msg(self, typ, j, body, subject=None):
  m = domish.Element(('jabber:client', 'message'))
  m['type'] = typ
  m['to'] = j
  if body: m.addElement('body').addContent(body)
  if subject: m.addElement('subject').addContent(subject)
  self.send(m)

 def call(self, f, *args, **kwargs):
  tc, self.tc = self.tc + 1, self.tc + 1
  self.th[tc] = (f, args, kwargs)
  if config.USE_THREADS: reactor.callInThread(self._call, f, tc, *args, **kwargs)
  else: self._call(f, tc, *args, **kwargs)
  try: self.th.pop(tc)
  except: self.log.err('Something wrong with threads management: can\'t self.th.pop(%s)' % (tc, ))

 def _call(self, f, tc, *args, **kwargs):
  try:
   self.log.log(escape('=== started thread #%s' % (tc, )), 1)
   try: f(*args, **kwargs)
   except:
    m = '; '.join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
    m = m.decode('utf8', 'replace')
    m = u'<font color=red><b>UNCATCHED ERROR:</b></font> %s\n<br/>\n(f, *args, *kwargs, thread) was <font color=grey>(%s)</font>' \
         % (escape(m), escape(repr((f, args, kwargs, tc))))
    self.log.err(m)
   self.log.log(escape('=== finished thread #%s' % (tc, )), 1)
  except:
   m = ''.join(traceback.format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
   print 'STOP: ', m
   self.log.err(escape(m))
   self.log.err('=== failed thread #%s' % (self.tc, ))

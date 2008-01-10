def rawxml(x):
 try:
  f = config.RAWXML
  f = open(f, 'a')
  f.write('[%s] receive: %s\n\n' % (time.strftime('%d:%m:%y %H:%M:%S'), x.toXml().encode('utf8')))
  f.close()
 except: pass

bot.wrapper.c.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, lambda x: bot.wrapper.x.addObserver('/*', rawxml))


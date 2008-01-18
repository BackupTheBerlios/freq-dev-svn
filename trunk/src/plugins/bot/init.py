BOOTUP_TIMESTAMP = time.time()
INFO = [[0, 0]]*5

def info_msg(x):
 INFO[4][0] += 1
 INFO[4][1] += len(x.toXml())

def info_timer():
 global INFO
 INFO = INFO[1:] + [[0, 0]]
 reactor.callLater(60, info_timer)

info_timer()

bot.wrapper.c.addBootstrap(xmlstream.STREAM_AUTHD_EVENT, lambda x: bot.wrapper.x.addObserver('/*', info_msg))
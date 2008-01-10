def stop_handler(t, s, p):
 s.msg(t, 'ok')
 reactor.callLater(1, reactor.stop)

bot.register_cmd_handler(stop_handler, '.stop', 50)
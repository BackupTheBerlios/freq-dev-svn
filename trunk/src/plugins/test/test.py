def test_handler(t, s, b):
 bot.wrapper.msg("chat", "pg@burdakov.pp.ru", "test!")
bot.wrapper.register_msg_handler(test_handler, "^test$")


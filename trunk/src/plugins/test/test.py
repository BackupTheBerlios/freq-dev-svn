def test_handler(t, s, b):
 bot.wrapper.msg(t, s, lang.msg("test.passed"))
bot.wrapper.register_msg_handler(test_handler, "^test$")

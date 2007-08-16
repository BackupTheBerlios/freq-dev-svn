def test_handler(t, s, p):
 if p: s.syntax(t, "test")
 else: s.lmsg(t, "test.passed")

bot.register_cmd_handler(test_handler, ".test")

def test_handler(t, s, p):
 if p: bot.muc.invalid_syntax(t, s)
 else: bot.muc.msg(t, s, lang.msg("test.passed", l=lang.getLang(s)))

bot.register_cmd_handler(test_handler, ".test")
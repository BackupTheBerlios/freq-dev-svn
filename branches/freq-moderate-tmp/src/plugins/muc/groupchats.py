def groupchats_handler(t, s, p):
 q = bot.g.keys()
 q = [i.replace(config.DEFAULT_MUC_SERVER, '') for i in q]
 s.lmsg(t, 'groupchats', ', '.join(q))

bot.register_cmd_handler(groupchats_handler, '.groupchats')
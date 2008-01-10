def groupchats_handler(t, s, p):
 q = bot.g.keys()
 q.sort(lambda x, y: len(bot.g[y].items)-len(bot.g[x].items))
 q = [i.replace(config.DEFAULT_MUC_SERVER, '') for i in q]
 s.lmsg(t, 'groupchats', u', '.join(q), len(q))

bot.register_cmd_handler(groupchats_handler, '.groupchats')
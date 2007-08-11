def whoami_handler(t, item, params):
 if params: item.syntax(t, ".whoami")
 else: item.lmsg(t, "muc_whois", item.nick, item.role, item.affiliation, item.show, item.status, time.strftime("%d.%m.%y %H:%M:%S"))

bot.register_cmd_handler(whoami_handler, ".whoami", g=1)

# "g=1" means, that this command avalable only in MUC


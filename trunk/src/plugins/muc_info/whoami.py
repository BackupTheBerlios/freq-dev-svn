def whoami_handler(t, item, params):
 if params: item.syntax(t, 'whoami')
 else: item.lmsg(t, "muc_whois", item.affiliation, item.role, item.show, item.status, time.strftime("%d.%m.%y %H:%M:%S", time.localtime(item.joined)), item.access())

bot.register_cmd_handler(whoami_handler, ".whoami", g=1)

# Note: "g=1" means that this command avalable only in MUC


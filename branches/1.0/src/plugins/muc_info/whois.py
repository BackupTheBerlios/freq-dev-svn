def whois_handler(t, item, params):
 try:
  q = item.room[params]
  item.lmsg(t, "muc_whois", q.affiliation, q.role, q.show, q.status, time.strftime("%d.%m.%y %H:%M:%S", time.localtime(q.joined)), q.access())
 except: item.syntax(t, 'whois')

bot.register_cmd_handler(whois_handler, ".whois", g=1)


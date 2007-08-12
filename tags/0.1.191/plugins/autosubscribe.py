def asu(p):
 t=str(p.getType());
 if t.count("subscribe"): JCON.send(xmpp.Presence(to=p.getFrom(), typ=t));
register_presence_handler(asu);
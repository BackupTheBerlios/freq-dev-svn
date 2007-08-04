def moderate(gc, nick, opt, value, id="freq_moderate", reason=None):
 if reason==None: reason=configget(gc, "moderatereason");
 siq=xmpp.Iq(to=gc);
 siq=xmpp.Iq(to=gc);
 siq.setID(id);
 siq.setType("set");
 siq.setQueryNS(xmpp.NS_MUC_ADMIN);
 siq.kids[0].addChild("item");
 q="nick";
 if re.search("^[^\@]+\@[^\@\/\ ]+$",nick): q="jid";
 siq.kids[0].kids[0].attrs={q:nick, opt:value};
 siq.kids[0].kids[0].addChild("reason");
 siq.kids[0].kids[0].kids[0].addData(reason);
 JCON.send(siq);
 return siq
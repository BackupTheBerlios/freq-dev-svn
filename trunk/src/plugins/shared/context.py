def context_replace(text, t, s):
 text = text.replace(r'%NICK%', s.nick).replace(r'%JID%', s.realjid).replace(r'%ROLE%', s.role).replace(r'%AFFILIATION%', s.affiliation)
 if s.room: text = text.replace(r'%ROOM%', s.room.jid)
 if s.room and s.room.bot: text = text.replace(r'%BOT%', s.room.bot.nick)
 return text
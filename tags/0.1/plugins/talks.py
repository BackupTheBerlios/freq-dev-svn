try: TALKS=read_file("static/talks.txt").split("\n");
except: TALKS=[];
TALKS=[i.strip().split("<>") for i in TALKS];
def mtalks(t, s, b):
 b=b.replace(get_nick(s[1]), "freQ");
 if (t=="public"):
  for i in TALKS:
   if re.match(i[0], b):
    q=random.choice(i[1].split("|"));
    q=q.replace("%n", s[2]);
    smsg(t, s[1], q);
register_message_handler(mtalks);
FLUD={0:time.time()};
def aflud(t, s, b):
 s1=s[1]+u"/"+s[2];
 try: ok=(PRS[s1].getAffiliation().lower()=="none")
 except: ok=0;
 if ok and (t=="public"):
  FLUD[s1]=FLUD.get(s1, 0)+len(b);
 if time.time()>FLUD[0]+5:
  FLUD.clear();
  FLUD[0]=time.time();
 for i in [j for j in FLUD.keys() if j<>0]:
  if FLUD[i]>int(configget(i.split("/")[0], "antifludlimit")):
   q=configget(s[1], "antifludtype");qt=0;
   while q[0:1]=="!":
    qt+=1;
    q=q[1:];
   if qt<3: m1="role"
   else: m1="affiliation";
   m2=("", "visitor", "none", "outcast")[qt];
   if qt>0: moderate(i.split("/")[0], i.split("/")[1], m1, m2, reason=q)
   else: smsg("public", s, q);
   FLUD.pop(i);
register_message_handler(aflud);

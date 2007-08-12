def joinall(gl):
 for i in gl: GROUPCHATS[i]={};
 for i in gl:
  join_groupchat(i);
  time.sleep(2);
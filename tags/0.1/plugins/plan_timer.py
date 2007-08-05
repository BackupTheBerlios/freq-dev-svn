LT={};
LT[0]=int(load_info("dynamic/LT"));
def tplan(x):
 for i in range(LT[0], int(time.time())+1):
  q=get_plan(i);
  if q:
   for j in q: eplan(j[0],j[1],j[2],j[3]);
 LT[0]=int(time.time());
 save_info("dynamic/LT",int(LT[0]));
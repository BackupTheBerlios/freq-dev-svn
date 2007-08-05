TDBU={0:time.time()}
def tdbu(c):
 if time.time()>TDBU[0]+60:
  TDBU[0]=time.time()
  try: db_update(c);
  except: c=0;
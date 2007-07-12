PSTART={};
def plan_start(x):
 if not PSTART:
  JCON.RegisterCycleHandler(tplan);
  JCON.RegisterCycleHandler(tdbu);
  PSTART[0]=1;
register_presence_handler(plan_start);
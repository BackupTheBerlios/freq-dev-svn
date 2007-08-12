def load_plan():
 try:
  f=file("dynamic/plan");
  p=pickle.load(f);
  f.close();
 except:
  p={};
 return p;
def save_plan(P):
 f=file("dynamic/plan","w");
 pickle.dump(P,f);
 f.close();
PLAN=load_plan();
def get_plan(t):
 if PLAN.has_key(int(t)):
  return PLAN.pop(t);
  save_plan(PLAN);
 return None;
def add_plan(t,x):
 if not PLAN.has_key(t): PLAN[t]=[];
 PLAN[t].append(x);
 save_plan(PLAN);
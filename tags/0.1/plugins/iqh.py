IQLIST={};
def fiqh(iqp):
 if IQLIST.has_key(iqp.getID()):
  thread.start_new(IQLIST[iqp.getID()][0],(iqp,IQLIST[iqp.getID()][1]));
  IQLIST.pop(iqp.getID());
register_iq_handler(fiqh);
def reg_iq(id, f, x): IQLIST[id]=(f,x);
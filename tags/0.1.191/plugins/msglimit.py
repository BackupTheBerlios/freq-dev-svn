#ML=load_info("dynamic/msglimit");
def get_msglimit(gc): return toint(configget(gc, "msglimit"), 400);
def set_msglimit(gc, value): configset(gc, "msglimit", value)
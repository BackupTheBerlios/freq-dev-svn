def save_info(f, x): write_file(f,str(x));
def load_info(f):
 try: return eval(read_file(f));
 except: return eval(read_file(f+".dist"))
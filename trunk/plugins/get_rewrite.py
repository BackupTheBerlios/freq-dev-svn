def get_rewrite_list(gc):
 x=[];
 if gc.count("/"): gc=gc[:gc.find("/")];
 if REWRITELIST.has_key(gc): x=REWRITELIST[gc];
 return x;
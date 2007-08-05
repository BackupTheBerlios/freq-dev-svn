def add_rewrite_list(gc, x):
 if gc.count("/"): gc=gc[:gc.find("/")];
 if not REWRITELIST.has_key(gc): REWRITELIST[gc]=[];
 REWRITELIST[gc].append([x[0], "".join(x[1:])]);
 save_info("dynamic/rewrite", REWRITELIST);
 return 0
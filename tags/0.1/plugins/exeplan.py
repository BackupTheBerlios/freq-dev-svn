def eplan(type,source,body,g):
 q=unicode(source[1]+u"/"+source[2]);
 set_ac(q,g);
 thread.start_new(cmd_parse, (source, type, re.search('^\.plan\ [^\ ]+\ ((.|\n)+)$',body).groups()[0]));
 time.sleep(1);
 set_ac(q,0);
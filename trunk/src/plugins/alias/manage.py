def alias_check(groupchat):
 if not ALIASES.has_key(groupchat):
  alias_load(groupchat)

def alias_load(groupchat):
 try: ALIASES[groupchat] = options.list2dict(options.optstringlist('aliases')[groupchat])
 except: ALIASES[groupchat] = {}

def alias_dump(groupchat):
 options.optstringlist('aliases')[groupchat] = options.dict2list(ALIASES.get(groupchat, {}))
 #print 'alias_dump'

def alias_get(groupchat, alias):
 alias_check(groupchat)
 return ALIASES[groupchat].get(alias)

def alias_set(groupchat, alias, value):
 alias_check(groupchat)
 ALIASES[groupchat][alias] = value
 alias_dump(groupchat)

def alias_del(groupchat, alias):
 alias_check(groupchat)
 ALIASES[groupchat].pop(alias)
 alias_dump(groupchat)

def alias_clear(groupchat):
 alias_check(groupchat)
 ALIASES[groupchat].clear()
 alias_dump(groupchat)

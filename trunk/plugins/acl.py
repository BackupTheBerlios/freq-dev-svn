#coding=utf8
def acl(s, l, m):
 if new_access(s[1]+u"/"+s[2])<l: return u"у вас недостаточно прав для этой команды, нужен уровень доступа хотя бы %d" % (l, );
 else: return m;
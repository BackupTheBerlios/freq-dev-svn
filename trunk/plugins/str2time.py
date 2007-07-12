def str2time(s):
 p=re.search('^([^\d]*)(\d*)([smhd\ ])',s).groups();
 return int(p[1])*{' ':1, 's':1, 'm':60, 'h':3600, 'd':86400}[p[2]]
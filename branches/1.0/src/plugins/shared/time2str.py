def time2str(t, rnd=None):
 minutes, seconds = divmod(t, 60)
 hours, minutes = divmod(minutes, 60)
 days, hours = divmod(hours, 24)
 if rnd: r = '%d sec.' % (seconds, )
 else: r = '%0.2f sec.' % (seconds, )
 if t>60: r = '%d min. %s' % (minutes, r)
 if t>3600: r = '%d h. %s' % (hours, r)
 if t>86400: r = '%d days, %s' % (days, r)
 return r


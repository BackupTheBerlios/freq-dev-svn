def info_handler(t, s, p):
 ut = time2str(time.time()-BOOTUP_TIMESTAMP, 1)
 mc = float(INFO[0][0]+INFO[1][0]+INFO[2][0]+INFO[3][0])/240
 sc = float(INFO[0][1]+INFO[1][1]+INFO[2][1]+INFO[3][1])/240
 if not mc: mc = 0.001
 s.lmsg(t, 'info', bot.version_name, bot.version_version, ut, '%0.2f' % (mc, ), int(sc/mc))

bot.register_cmd_handler(info_handler, '.info')
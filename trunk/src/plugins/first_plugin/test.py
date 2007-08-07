print "hello! i'm test plugin"
def areply(t, s, b):
 print "got msg"+t+s+b
 #bot.wrapper.msg(typ=t, j=s, body=b)
bot.wrapper.register_msg_handler(areply, ".*")

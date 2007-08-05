#coding=utf8
def save_wtf(x):
 leave_groupchat("main@conference.burdakov.pp.ru");
 p=u'dfn %s=%s' % (x[1], x[2]);
 join_groupchat('main@conference.burdakov.pp.ru', x[0]+u" через freQ");
 JCON.send(xmpp.Message('main@conference.burdakov.pp.ru/adgjm', p,'chat'));
 #time.sleep(1);
 #msg('soul@jabbus.org/jabbus.org','wtfrand');
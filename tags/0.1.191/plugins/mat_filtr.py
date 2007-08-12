#$ neutron_plugin 01
# -*- coding: utf-8  -*-
import string

def mat(type, source,mat2):
    mat=string.lower(mat2)
    mat_table='/home/dicson/bot/neutron/plugins/mat_table.ll'
    mat_iskluch='/home/dicson/bot/neutron/plugins/mat_iskluch.ll'
    fpm = open(mat_table, 'r')
    fpi = open(mat_iskluch, 'r')
    fppi=1
    while fppi:
        fppi= fpi.readline()
        linei= unicode(fppi.strip(),'windows-1251')
        if linei == mat:
            return 0
    
    while  1 :
        line = fpm.readline()
        if not line:
            return 0
        line2= unicode(line.strip(),'windows-1251')
        if line2 in mat:
            return u'ЗАКАНЧИВАЙ МАТЕРИТЬСЯ'

def kick(type, source, parameters):
	if parameters.strip():### Если в сообщении указан ник
		nick = parameters.strip()
		groupchat = source[1]
		if GROUPCHATS.has_key(groupchat) and GROUPCHATS[groupchat].has_key(parameters.strip()):
			if parameters.strip():### Если в сообщении указан ник
				nick = parameters.strip()
			else:
				parameters = source[2]
				nick = source[2]	
			groupchat = source[1]	
			last_iq = xmpp.Iq('set',to=groupchat)
			last_iq.setQueryNS('http://jabber.org/protocol/muc#admin')
			qp = last_iq.getTag('query')
			qp.setTagAttr('item','nick','none')
			nick =parameters.strip()
			p = qp.getTag('item')
			p.setAttr('nick',nick)
			p.setAttr('role' ,'none')
			p.setTagData('reason',val=u'За ругательства!!!')
##			print last_iq
			versions = JCON.send(last_iq)
		else:
			smsg(type, source, 'User Not In Chat [' + parameters + ']')
	else:
		smsg(type, source, 'Insert Nick ')



def handler_mat_message(type, source,mat2):
    
    nik2='neutron2'
    if source[2] != nik2:
        maty=mat(type, source,mat2)
        if maty:
            smsg(type, source,maty)
            kick(type, source,source[2])
#while  1 :
 #   print mty(unicode(raw_input(u'ввод '),'windows-1251'))
#register_message_handler(handler_mat_message)

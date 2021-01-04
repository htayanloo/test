# -*- coding: utf-8 -*-
import logging
import sys

import smpplib.gsm
import smpplib.client
import smpplib.consts

# This is a small script using https://github.com/podshumok/python-smpplib
# to generate some SMS load on OsmoNITB via its SMPP interface

# if you want to know what's happening
logging.basicConfig(level = logging.DEBUG,
    format = "%(levelname)s %(filename)s:%(lineno)d %(message)s")

def send_message(dest, string):
    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(string,encoding=smpplib.consts.SMPP_ENCODING_ISO10646)
    print("type : %s" % encoding_flag)
    print("type : %s" % type(encoding_flag))
    print('Sending SMS "%s" to %s' % (string, dest))
    for part in parts:
        print("Parts :::::: %s" % part)
        pdu = client.send_message(
            source_addr_ton=0,
            source_addr_npi=0,
            source_addr='988938004',
            dest_addr_ton=1,
            dest_addr_npi=1,
            destination_addr=dest,
            short_message=part,
            data_coding=24,
#            esm_class=msg_type_flag,
            esm_class=smpplib.consts.SMPP_MSGMODE_FORWARD,
            registered_delivery=True,
    )
    print(pdu.sequence)


client = smpplib.client.Client('10.203.10.74', 2556)
#client = smpplib.client.Client('10.15.82.3', 2556)

# Print when obtain message_id
client.set_message_sent_handler(
    lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
client.set_message_received_handler(
    lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))

client.connect()
client.bind_transceiver(system_id='SQM', password='PASQM^$!',interface_version=34,system_type="SMPP",addr_ton=0,addr_npi=0)

destinations = ['989128387233']
#destinations = ['989392760478']

for dest in destinations:
    print("start Send -Messag")
    message_text ='این اولین پیامک تست پایلوت پروژه جاده هوشمند میباشد'
#    message_text = message_text.encode( "utf-8")
    print(message_text)
    send_message(dest, message_text)

client.listen()


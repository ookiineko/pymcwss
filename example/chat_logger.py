# -*- coding: utf-8 -*-
"""
chat logger example
"""
from pymcwss.mcwss import MCWSS
from pymcwss.pewsapi import event_player_msg, \
    get_head, get_body, get_prop, get_msg_purpose, \
    purpose_event, get_event_name, get_msg_type, msg_chat, \
    msg_say, msg_tell, gen_all_subs, gen_sub, par_player_msg
from websockets.legacy.server import WebSocketServerProtocol

from util import get_lan_ip


class ChatLogger(MCWSS):
    """
    chat logger
    """

    def __init__(self, ws: WebSocketServerProtocol):
        MCWSS.__init__(self, ws)
        self.__subs = {
            event_player_msg
        }

    @classmethod
    def on_start(cls, _host: str, port: int):
        """
        on server start
        """
        MCWSS.on_start(_host, port)
        print('/connect %s:%d' % (get_lan_ip(), port))

    async def on_conn(self):
        """
        on client connected
        """
        await MCWSS.on_conn(self)
        print('Minecraft connected')
        for packet in gen_all_subs(self.__subs, True):
            await self.send(packet)
        for sub in self.__subs:
            packet = gen_sub(sub)
            await self.send(packet)

    async def on_dc(self):
        """
        on client disconnected
        """
        await MCWSS.on_dc(self)
        print('Minecraft disconnected')

    async def on_recv(self, packet: dict):
        """
        on received client packet
        """
        await MCWSS.on_recv(self, packet)
        head = get_head(packet)
        msg_purpose = get_msg_purpose(head)
        if msg_purpose == purpose_event:
            body = get_body(packet)
            event_name = get_event_name(body)
            if event_name == event_player_msg:
                prop = get_prop(body)
                msg_type = get_msg_type(prop)
                if msg_type in (msg_chat, msg_say, msg_tell):
                    sender, receiver, msg = par_player_msg(prop)
                    if msg_type == msg_tell:
                        print('<{0}> {0} whispers to {1}: {2}'.format(sender, receiver, msg))
                    else:
                        print(('<%s> %s' % (sender, msg)) if msg_type == msg_chat else msg)


wss_port = 14514
ChatLogger.start(wss_port)

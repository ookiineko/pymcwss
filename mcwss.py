# -*- coding: utf-8 -*-
"""
Minecraft WebSocket server
"""

from abc import ABC, abstractmethod
from asyncio import get_event_loop, AbstractEventLoop
from json import loads, dumps, JSONDecodeError
from traceback import format_exc

from websockets.exceptions import ConnectionClosed
from websockets.legacy.server import serve, WebSocketServerProtocol


class MCWSS(ABC):
    """
    Minecraft WebSocket server
    """

    def __init__(self, ws: WebSocketServerProtocol):
        self.__ws = ws
        self.connected = False

    async def main_loop(self):
        """
        sever main loop
        """
        await self.on_conn()
        while self.__ws.open:
            try:
                data = await self.__ws.recv()
                packet = loads(data)
                await self.on_recv(packet)
            except (ConnectionClosed, JSONDecodeError):
                print(format_exc())
                break
        await self.on_dc()

    async def send(self, packet: dict):
        """
        send packet
        """
        if packet and self.connected:
            await self.__ws.send(dumps(packet))

    @abstractmethod
    async def on_conn(self):
        """
        on client connected
        """
        self.connected = True

    @abstractmethod
    async def on_dc(self):
        """
        on client disconnected
        """
        self.connected = False

    @abstractmethod
    async def on_recv(self, packet: dict):
        """
        on received client packet
        """
        pass

    @classmethod
    async def ws_handler(cls, ws: WebSocketServerProtocol, _path: str):
        """
        WebSocket handler
        """
        instance = cls(ws)
        await instance.main_loop()

    @classmethod
    @abstractmethod
    def on_start(cls, host: str, port: int):
        """
        on server start
        """
        pass

    @classmethod
    def start(
            cls,
            port: int,
            host: str = '',
            event_loop: AbstractEventLoop = get_event_loop()
    ):
        """
        start server
        """
        wss = serve(cls.ws_handler, host, port)
        event_loop.run_until_complete(wss)
        cls.on_start(host, port)
        event_loop.run_forever()

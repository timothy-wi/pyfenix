"""API base class."""

import asyncio
from typing import Tuple

class API:
    """Base class for all client API implementations."""

    def __init__(self) -> None:
        self._done = False

    async def connect(self, server: Tuple[str, int]) -> None:
        """
        Connect to a server.

        Must be implemented by subclasses.
        """
        raise NotImplementedError

    async def listen(self, fut: asyncio.Future) -> None:
        """
        Listen for events.
        """
        while not self._done:
            await asyncio.sleep(0.2)
            await self.recv_event()

        fut.set_result(None)

    async def send(self, msg: str) -> None:
        """
        Send a message to the server.

        Must be implemented by subclasses.
        """
        raise NotImplementedError

    async def recv_event(self) -> None:
        """
        Handle one event from server.

        Must be implemented by subclasses.
        """
        raise NotImplementedError


class NoConnectionError(Exception):
    """Represents an attempt to use the API without a connection"""

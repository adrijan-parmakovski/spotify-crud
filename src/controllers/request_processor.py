from abc import ABC, abstractmethod
from asyncio import Event, Queue, Semaphore, create_task, gather, sleep
from asyncio.exceptions import CancelledError
from typing import Tuple
from uuid import UUID, uuid4

import aiohttp
import requests


class AsyncRequestHandler:
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def send_request(self, request: dict):
        async with self.session.request(**request) as response:
            try:
                resp = await response.json()
            except Exception as exc:
                print(type(exc), exc)
                resp = await response.read()
            return (resp, response.headers, response.status)

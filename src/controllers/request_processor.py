from asyncio import Semaphore
from typing import Tuple

import aiohttp


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


class AsyncProcessor:
    _MAX_CONCURRENT_REQUESTS = 30

    def __init__(self) -> None:
        self._session = None
        self._request_handler = None
        self._semaphore = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        self._request_handler = AsyncRequestHandler(self._session)
        self._semaphore = Semaphore(self._MAX_CONCURRENT_REQUESTS)

    async def __aexit__(self, *args):
        return self._session.close()

    async def submit_request(self, request: dict) -> Tuple[dict | str, dict, int]:
        async with self._semaphore:
            return await self._request_handler.submit_request(request)

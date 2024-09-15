import asyncio
import json

import aiohttp
from aiohttp import ClientSession

from assignment_4.constants import INDENT


class DataRetriever:
    def __init__(self, output_file: str, posts_num: int, urls: list) -> None:
        self.output_file = open(output_file, "w")
        self.number_of_posts = posts_num
        self.counter = 0
        self.lock = asyncio.Lock()
        self.urls = urls

    def write(self, data: str) -> None:
        self.output_file.write(data)

    def close(self) -> None:
        self.output_file.close()

    async def fetch_url(self, session: ClientSession, url: str) -> None:
        try:
            async with session.get(url) as response:
                data = await response.json()
                formatted_data = json.dumps(data, indent=4)
                formatted_data = formatted_data.replace("\n", "\n" + INDENT)
                formatted_data = INDENT + formatted_data
            async with self.lock:
                if self.counter != self.number_of_posts - 1:
                    formatted_data += ",\n"
                    self.counter += 1
                else:
                    formatted_data += "\n"
                self.write(formatted_data)
        except aiohttp.ClientError as e:
            print(f"Error fetching {url}: {e}")
            return

    async def fetch_all_urls(self) -> None:
        async with ClientSession() as session:
            for url in self.urls:
                await self.fetch_url(session, url)

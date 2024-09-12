import asyncio
import json
import time

import aiohttp

from assignment_3.constants import INDENT, OUTPUT_FILE, POSTS_NUM, URL

urls = [URL + str(i) for i in range(1, POSTS_NUM + 1)]
counter = 0


async def fetch_url(
    session: aiohttp.ClientSession, url: str, lock: asyncio.Lock
) -> None:
    global counter
    try:
        async with session.get(url) as response:
            data = await response.json()
            formatted_data = json.dumps(data, indent=4).replace("\n", "\n  ")
            formatted_data = INDENT + formatted_data
        async with lock:
            if counter != POSTS_NUM - 1:
                formatted_data += ",\n"
                counter += 1
            else:
                formatted_data += "\n"
            with open(OUTPUT_FILE, "a") as file:
                file.write(formatted_data)
    except aiohttp.ClientError as e:
        print(f"Error fetching {url}: {e}")
        return


async def fetch_all_urls(all_urls: list) -> None:
    lock = asyncio.Lock()
    async with aiohttp.ClientSession() as session:
        for url in all_urls:
            await fetch_url(session, url, lock)


async def main():
    start = time.time()

    with open(OUTPUT_FILE, "w") as f:
        f.write("[\n")

    await fetch_all_urls(urls)

    with open(OUTPUT_FILE, "a") as f:
        f.write("]")

    print(time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())

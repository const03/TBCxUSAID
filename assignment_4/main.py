import asyncio
import time

from assignment_4.constants import OUTPUT_FILE, POSTS_NUM, URL
from assignment_4.data_retriever import DataRetriever


async def main():
    start = time.time()

    urls = [URL + str(i) for i in range(1, POSTS_NUM + 1)]

    data_retriever = DataRetriever(OUTPUT_FILE, POSTS_NUM, urls)
    data_retriever.write("[\n")

    await data_retriever.fetch_all_urls()

    data_retriever.write("]")
    data_retriever.close()

    print(time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())

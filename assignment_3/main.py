import time
from concurrent.futures import ThreadPoolExecutor

from assignment_3.constants import MAX_WORKERS, OUTPUT_FILE, POSTS_NUM, URL
from assignment_3.data_retriever import DataRetriever


def main() -> None:
    data_retriever = DataRetriever(OUTPUT_FILE, POSTS_NUM)
    data_retriever.write("[\n")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for i in range(1, data_retriever.get_number_of_posts() + 1):
            executor.submit(data_retriever.get_data, URL + str(i))

    data_retriever.write("]")
    data_retriever.close()

    print(time.time() - start_time)


if __name__ == "__main__":
    main()

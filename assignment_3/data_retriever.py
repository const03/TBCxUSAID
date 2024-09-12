import json
import threading

import requests

from assignment_3.constants import INDENT


class DataRetriever:
    def __init__(self, output_file: str, number_of_posts: int) -> None:
        self.output_file = open(output_file, "w")
        self.number_of_posts = number_of_posts
        self.counter = 0
        self.lock = threading.Lock()

    def write(self, data: str) -> None:
        self.output_file.write(data)

    def close(self) -> None:
        self.output_file.close()

    def get_data(self, url: str) -> None:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

        if response.status_code == 200:
            data = response.json()

            with self.lock:
                formatted = json.dumps(data, indent=4).replace("\n", "\n  ")
                formatted = INDENT + formatted

                if self.counter != self.number_of_posts - 1:
                    self.counter += 1
                    formatted += ",\n"
                else:
                    formatted += "\n"

                self.write(formatted)
        else:
            print(f"Error: {response.status_code}")

    def get_number_of_posts(self) -> int:
        return self.number_of_posts

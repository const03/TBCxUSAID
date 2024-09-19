from dataclasses import dataclass

from assignment_5.abstract_dao import AbstractDAO


@dataclass
class BooksDAO(AbstractDAO):
    def __post_init__(self) -> None:
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        fields = """(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    pages INTEGER,
                    publication_date DATE,
                    author_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors(id)
                    )"""
        self.fields = fields
        self.table_name = "books"

    def insert(self, book: list) -> None:
        query = (
            f"INSERT INTO {self.table_name} "
            f"(title, category, pages, publication_date, author_id)"
            f" VALUES (?, ?, ?, ?, ?)"
        )
        self.cursor.execute(query, book)
        self.connection.commit()

    def insert_all(self, books: list) -> None:
        query = (
            f"INSERT INTO {self.table_name} "
            f"(title, category, pages, publication_date, author_id)"
            f" VALUES (?, ?, ?, ?, ?)"
        )
        self.cursor.executemany(query, books)
        self.connection.commit()

    def get_book_with_most_pages(self) -> list:
        query = f"SELECT * FROM {self.table_name} ORDER BY pages DESC"
        self.cursor.execute(query)
        book = self.cursor.fetchone()
        return book

    def get_average_number_of_pages(self) -> float:
        query = f"""SELECT AVG(pages) FROM {self.table_name}"""
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

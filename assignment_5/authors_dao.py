from dataclasses import dataclass

from assignment_5.abstract_dao import AbstractDAO


@dataclass
class AuthorsDAO(AbstractDAO):
    def __post_init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        fields = """(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    birth_date DATE,
                    birth_place TEXT
                    )"""
        self.fields = fields
        self.table_name = "authors"

    def insert(self, author: list) -> None:
        query = (
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name, birth_date, birth_place)"
            f" VALUES (?, ?, ?, ?)"
        )
        self.cursor.execute(query, author)
        self.connection.commit()

    def insert_all(self, authors: list) -> None:
        query = (
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name, birth_date, birth_place)"
            f" VALUES (?, ?, ?, ?)"
        )
        self.cursor.executemany(query, authors)
        self.connection.commit()

    def get_youngest_author(self) -> list:
        query = f"SELECT * FROM {self.table_name} ORDER BY birth_date DESC"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_authors_with_no_books(self) -> list:
        authors = []
        query = (
            f"SELECT first_name, last_name FROM {self.table_name}"
            f" WHERE id NOT IN (SELECT author_id FROM books)"
        )
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for author in results:
            authors.append(f"{author[0]} {author[1]}")
        return authors

    def get_five_authors_with_more_than_three_books(self) -> list:
        authors = []
        query = (
            f"SELECT first_name, last_name FROM {self.table_name} "
            f"WHERE id IN (SELECT author_id FROM books "
            f"GROUP BY author_id HAVING COUNT(*) > 3)"
        )
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for author in results[:5]:
            authors.append(f"{author[0]} {author[1]}")
        return authors

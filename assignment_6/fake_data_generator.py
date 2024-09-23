import random
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from faker import Faker

from assignment_6.models import Author, Book, BookAndAuthor

MAX_AUTHORS = 7
MIN_AGE = 10
MIN_PAGES = 50
MAX_PAGES = 1000


@dataclass
class FakeDataGenerator:
    number_of_books: int
    number_of_authors: int
    faker: Faker = field(default_factory=Faker)

    def book(self, book_id: int) -> tuple[Book, list[int]]:
        num_authors = random.randint(1, MAX_AUTHORS)

        list_of_authors = []
        for i in range(num_authors):
            list_of_authors.append(random.randint(0, self.number_of_authors))
        list_of_authors = list(set(list_of_authors))

        book = Book(
            id=book_id,
            title=self.faker.sentence(nb_words=4),
            category=self.faker.word(),
            pages=random.randint(MIN_PAGES, MAX_PAGES),
            publication_date=datetime.strptime(self.faker.date(), "%Y-%m-%d").date(),
        )
        return book, list_of_authors

    def author(self) -> Author:
        author = Author(
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            birth_date=self.faker.date_of_birth(minimum_age=MIN_AGE),
            birth_place=self.faker.city(),
        )
        return author

    def list_of_books(self) -> tuple[Any, Any]:
        books = []
        book_and_author = []
        for i in range(self.number_of_books):
            book, list_of_authors = self.book(i)
            books.append(book)
            elems = [
                BookAndAuthor(book_id=book.id, author_id=author_id)
                for author_id in list_of_authors
            ]
            book_and_author += elems
        return books, book_and_author

    def list_of_authors(self) -> list[Author]:
        authors = []
        for i in range(self.number_of_authors):
            authors.append(self.author())
        return authors

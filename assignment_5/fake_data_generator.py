import random
from dataclasses import dataclass, field

from faker import Faker

from assignment_5.constants import (
    MAX_PAGES,
    MIN_AGE,
    MIN_PAGES,
    NUMBER_OF_AUTHORS,
    NUMBER_OF_BOOKS,
)


@dataclass
class FakeDataGenerator:
    faker: Faker = field(default_factory=Faker)

    def book(self) -> list:
        book = [
            self.faker.sentence(nb_words=4),
            self.faker.word(),
            random.randint(MIN_PAGES, MAX_PAGES),
            self.faker.date(),
            random.randint(0, NUMBER_OF_AUTHORS),
        ]
        return book

    def author(self) -> list:
        author = [
            self.faker.first_name(),
            self.faker.last_name(),
            self.faker.date_of_birth(minimum_age=MIN_AGE),
            self.faker.city(),
        ]
        return author

    def list_of_books(self) -> list:
        books = []
        for i in range(NUMBER_OF_BOOKS):
            book = [
                self.faker.sentence(nb_words=4),
                self.faker.word(),
                random.randint(MIN_PAGES, MAX_PAGES),
                self.faker.date(),
                random.randint(0, NUMBER_OF_AUTHORS),
            ]
            books.append(book)
        return books

    def list_of_authors(self) -> list:
        authors = []
        for i in range(NUMBER_OF_AUTHORS):
            author = [
                self.faker.first_name(),
                self.faker.last_name(),
                self.faker.date_of_birth(minimum_age=MIN_AGE),
                self.faker.city(),
            ]
            authors.append(author)
        return authors

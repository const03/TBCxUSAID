from dataclasses import dataclass
from typing import Any

from sqlalchemy import func

from assignment_6.models import Book


@dataclass
class BookRepository:
    session: Any

    def add_book(self, book: Book) -> None:
        self.session.add(book.to_list())
        self.session.commit()

    def add_books(self, books: list[Book]) -> None:
        self.session.add_all(books)
        self.session.commit()

    def get_largest_book(self) -> Book:
        book = self.session.query(Book).order_by(Book.pages.desc()).first()
        return book

    def get_average_number_of_pages(self) -> float:
        average_pages = self.session.query(func.avg(Book.pages)).scalar()
        return float(average_pages)

from dataclasses import dataclass
from typing import Any

from sqlalchemy import func

from assignment_6.models import Author, BookAndAuthor


@dataclass
class BookAndAuthorRepository:
    session: Any

    def add_book_author_pairs(self, pairs: list[BookAndAuthor]) -> None:
        self.session.add_all(pairs)
        self.session.commit()

    def get_authors_with_n_books(
        self, num_of_books: int, num_of_authors: int
    ) -> list[Author]:
        authors_with_n_books = (
            self.session.query(Author)
            .join(BookAndAuthor)
            .group_by(Author.id)
            .having(func.count(BookAndAuthor.book_id) > num_of_books)
            .limit(num_of_authors)
            .all()
        )

        return list(authors_with_n_books)

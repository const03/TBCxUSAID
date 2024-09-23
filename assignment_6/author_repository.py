from dataclasses import dataclass
from typing import Any

from sqlalchemy import select

from assignment_6.models import Author, BookAndAuthor


@dataclass
class AuthorRepository:
    session: Any

    def add_author(self, author: Author) -> None:
        self.session.add(author)
        self.session.commit()

    def add_authors(self, authors: list[Author]) -> None:
        self.session.add_all(authors)
        self.session.commit()

    def get_youngest_author(self) -> Author:
        youngest_author = (
            self.session.query(Author).order_by(Author.birth_date.desc()).first()
        )
        return youngest_author

    def get_authors_with_no_books(self) -> list[Any]:
        subquery = select(BookAndAuthor.author_id).distinct()
        authors_without_books = (
            self.session.query(Author).filter(~Author.id.in_(subquery)).all()
        )

        return list(authors_without_books)

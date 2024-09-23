from typing import Any

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    publication_date = Column(Date, nullable=False)

    authors = relationship(
        "Author", secondary="book_and_author", back_populates="books"
    )

    def to_list(self) -> list[Any]:
        author_names = [
            f"{author.first_name} {author.last_name}" for author in self.authors
        ]
        return [
            self.id,
            self.title,
            self.category,
            self.pages,
            self.publication_date.strftime("%B %d, %Y"),
            author_names,
        ]


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    birth_place = Column(String, nullable=False)

    books = relationship("Book", secondary="book_and_author", back_populates="authors")

    def to_list(self) -> list[Any]:
        # book_titles = [book.title for book in self.books]
        return [
            self.id,
            self.first_name,
            self.last_name,
            self.birth_date.strftime("%B %d, %Y"),
            self.birth_place,
        ]

    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class BookAndAuthor(Base):
    __tablename__ = "book_and_author"

    book_id = Column(Integer, ForeignKey("book.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)

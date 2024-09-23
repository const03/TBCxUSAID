from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from assignment_6.author_repository import AuthorRepository
from assignment_6.book_and_author_repository import BookAndAuthorRepository
from assignment_6.book_repository import BookRepository
from assignment_6.fake_data_generator import FakeDataGenerator
from assignment_6.models import Base

DATABASE = "assignment_6.db"
NUMBER_OF_BOOKS = 1000
NUMBER_OF_AUTHORS = 500


def insert_all_authors(author: AuthorRepository, fake: FakeDataGenerator) -> None:
    author.add_authors(fake.list_of_authors())


def insert_all_books(
    book: BookRepository,
    book_and_author: BookAndAuthorRepository,
    fake: FakeDataGenerator,
) -> None:
    books, book_author_pairs = fake.list_of_books()
    book.add_books(books)
    book_and_author.add_book_author_pairs(book_author_pairs)


def main() -> None:
    fake = FakeDataGenerator(NUMBER_OF_BOOKS, NUMBER_OF_AUTHORS)

    engine = create_engine(f"sqlite:///{DATABASE}")
    session = sessionmaker(bind=engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = session()

    book_repository = BookRepository(session)
    author_repository = AuthorRepository(session)
    book_and_author_repository = BookAndAuthorRepository(session)

    insert_all_authors(author_repository, fake)
    insert_all_books(book_repository, book_and_author_repository, fake)

    book = book_repository.get_largest_book()
    print("Book with most pages:")
    print(book.to_list())

    average = book_repository.get_average_number_of_pages()
    print(f"\nAverage number of pages is {average}")

    youngest = author_repository.get_youngest_author()
    print("\nYoungest author:")
    print(youngest.to_list())

    authors = author_repository.get_authors_with_no_books()
    print("\nAuthor(s) with no books:")
    if len(authors) != 0:
        for author in authors:
            print(author.name())
    else:
        print("Such authors can't be found")

    num_of_authors = 5
    num_of_books = 3
    authors = book_and_author_repository.get_authors_with_n_books(
        num_of_books, num_of_authors
    )
    print(f"\n{num_of_authors} author(s) with more than {num_of_books} books:")
    if len(authors) != 0:
        for author in authors:
            print(author.name())
    else:
        print("Such authors can't be found")


if __name__ == "__main__":
    main()

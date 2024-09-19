from assignment_5.authors_dao import AuthorsDAO
from assignment_5.books_dao import BooksDAO
from assignment_5.constants import DATABASE, NUMBER_OF_AUTHORS, NUMBER_OF_BOOKS
from assignment_5.fake_data_generator import FakeDataGenerator


def insert_one_by_one(books_dao, authors_dao, fake) -> None:
    for i in range(NUMBER_OF_BOOKS):
        books_dao.insert(fake.book())

    for i in range(NUMBER_OF_AUTHORS):
        authors_dao.insert(fake.author())


def insert_all(books_dao, authors_dao, fake) -> None:
    books_dao.insert_all(fake.list_of_books())
    authors_dao.insert_all(fake.list_of_authors())


def main():
    fake = FakeDataGenerator()
    books_dao = BooksDAO(DATABASE)
    authors_dao = AuthorsDAO(DATABASE)

    authors_dao.clear()
    authors_dao.create()

    books_dao.clear()
    books_dao.create()

    # insert_one_by_one(books_dao, authors_dao, fake)
    insert_all(books_dao, authors_dao, fake)

    book = books_dao.get_book_with_most_pages()
    print("Book with most pages:")
    print(book)

    average = books_dao.get_average_number_of_pages()
    print(f"\nAverage number of pages is {average}")

    youngest = authors_dao.get_youngest_author()
    print("\nYoungest author:")
    print(youngest)

    authors = authors_dao.get_authors_with_no_books()
    print("\nAuthor(s) with no books:")
    if authors is not None:
        for author in authors:
            print(author)
    else:
        print("Such authors can't be found")

    authors = authors_dao.get_five_authors_with_more_than_three_books()
    print("\nAuthor(s) with more than 3 books:")
    if authors is not None:
        for author in authors:
            print(author)
    else:
        print("Such authors can't be found")

    books_dao.disconnect()
    authors_dao.disconnect()


if __name__ == "__main__":
    main()

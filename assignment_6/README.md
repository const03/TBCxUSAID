# Database Operations with SQLAlchemy

## Overview

This project involves creating an SQLite database with three tables: **book**, **author**, and a many-to-many relationship table **book_and_author**. The database is populated with randomly generated data using the **Faker** library. The project utilizes **SQLAlchemy** for ORM (Object-Relational Mapping) to manage database operations efficiently.

## Features

- **Three Tables**:
  - **book**: Contains information about books, including title, category, page count, publication date, and related authors.
  - **author**: Contains details about authors, including first name, last name, date of birth and place of birth.
  - **book_and_author**: A join table that establishes the many-to-many relationship between books and authors.
  
- **Random Data Generation**:
  - 500 random authors and 1000 random books are generated using the `Faker` library.
  
- **Implemented SQL Queries**:
  - Find and print the book with the highest page count.
  - Calculate and display the average page count of all books.
  - Find and print the youngest author.
  - List authors who haven't published any books.
  - Find 5 authors who have written more than 3 books.

## Structure

- **`models.py`**: Contains the `Book`, `Author`, and `BookAndAuthor` models representing the corresponding tables.
- **`BookRepository`**: A class implementing the repository pattern for operations on the `book` table.
- **`AuthorRepository`**: A class implementing the repository pattern for performing operations related to the `author` table.
- **`BookAndAuthorRepository`**: A class managing the many-to-many relationships between books and authors.
- **`FakeDataGenerator`**: A class that uses the `Faker` library to generate random book and author data for the database.

## Database Schema

- **Book Table**:
  - `id` (Primary Key)
  - `title` (Text)
  - `category` (Text)
  - `pages` (Integer)
  - `publication_date` (Date)

- **Author Table**:
  - `id` (Primary Key)
  - `first_name` (Text)
  - `last_name` (Text)
  - `birth_date` (Date)
  - `birth_place` (Text)

- **Book and Author Table**:
  - `book_id` (Foreign Key to `Book` table)
  - `author_id` (Foreign Key to `Author` table)

## Dependencies

- **Python 3.11**
- **SQLAlchemy**: Used for database operations. 
- **Faker**: Used for generating random data. Install via pip: `pip install faker`

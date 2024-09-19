# SQLite Database Operations with Python

## Overview

This project involves creating an SQLite database with two tables: **books** and **authors**. The database is populated with randomly generated data using the **Faker** library, and various SQL operations are performed to retrieve specific information. The project implements the Data Access Object (DAO) pattern for managing database operations.

## Features

- **Two Tables**:
  - **books**: Contains information about books, including title, category, page count, publication date, and the author's ID.
  - **authors**: Contains details about authors, including first name, last name, birth_date, and place of birth.
  
- **Random Data Generation**:
  - 500 random authors and 1000 random books are generated using the `Faker` library.
  
- **Implemented SQL Queries**:
  - Find and print the book with the highest page count.
  - Calculate and display the average page count of all books.
  - Find and print the youngest author.
  - List authors who haven't published any books.
  - Find 5 authors who have written more than 3 books.

## Structure

- **`AbstractDAO`**: An abstract class defining the common interface for database operations.
- **`BooksDAO`**: A class implementing the DAO interface for operations on the `books` table.
- **`AuthorsDAO`**: A class implementing the DAO interface for performing operations related to the `authors` table.
- **`FakeDataGenerator`**: A class that uses the `Faker` library to generate random book and author data for the database.

## Database Schema

- **Books Table**:
  - `id` (Primary Key)
  - `title` (Text)
  - `category` (Text)
  - `pages` (Integer)
  - `publication_date` (Date)
  - `author_id` (Foreign Key to `Authors` table)

- **Authors Table**:
  - `id` (Primary Key)
  - `first_name` (Text)
  - `last_name` (Text)
  - `birth_date` (Date)
  - `birth_place` (Text)


## Dependencies

- **Python 3.11**
- **SQLite3**
- **Faker**: Used for generating random data. Install via pip: `pip install faker`


## Code Quality

This project follows standard coding practices and uses the following tools for linting, formatting, and type checking:

- **Ruff**: Fast Python linter to enforce PEP8 and other coding standards.
- **Flake8**: A Python linting tool used to ensure code quality.
- **Black**: A Python code formatter that enforces consistent code style.
- **Mypy**: A static type checker for Python.
- **isort**: A Python utility to sort imports in the code.
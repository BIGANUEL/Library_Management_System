# Library Management System

## Overview
This Library Management System is a Python-based application that interacts with a MySQL database to store, retrieve, and manage book information. It allows users to add books, search for books by title, list all books in the library, and delete books by their unique ID.

The project is a simple demonstration of how Python can be used to interact with a relational database like MySQL using the `mysql-connector-python` library.

## Features
- **Add a Book**: Insert a new book into the library with details like title, author, and ISBN.
- **Search for a Book**: Look up books by their title.
- **List All Books**: View all books currently available in the library.
- **Delete a Book**: Remove a book from the library by its ID.

## Database Schema

The system uses a MySQL database named `library_management` with a single table `Books` that has the following structure:

| Column | Data Type      | Description                          |
|--------|----------------|--------------------------------------|
| id     | INT (Primary Key, Auto-Increment) | Unique identifier for each book |
| title  | VARCHAR(255)    | The title of the book                |
| author | VARCHAR(255)    | The author of the book               |
| ISBN   | VARCHAR(255)    | The International Standard Book Number (ISBN) |

## Prerequisites
Before running this application, make sure you have the following installed:
- Python 3.x
- MySQL server
- `mysql-connector-python` package

Install the MySQL connector package using pip:
```bash
pip install mysql-connector-python

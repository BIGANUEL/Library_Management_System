import mysql.connector

# Establishes a connection to the MySQL database
def connect_to_db():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "********",  # Replace with your actual password
        database = "library_management"
    )
    return mydb

# Adds a new book to the 'Books' table with given title, author, and ISBN
def add_book(title, author, isbn):
    mydb = connect_to_db()  # Connect to the database
    mycursor = mydb.cursor()

    sql = "INSERT INTO Books(title, author, ISBN) VALUES(%s, %s, %s)"
    val = (title, author, isbn)

    mycursor.execute(sql, val)  # Execute the SQL query
    mydb.commit()  # Commit changes to the database
    print(f"{title} added successfully")

    # Close cursor and connection
    mycursor.close()
    mydb.close()

# Searches for books by title in the 'Books' table
def search_book(title):
    try:
        mydb = connect_to_db()  # Connect to the database
        mycursor = mydb.cursor()

        sql = "SELECT * FROM Books WHERE title = %s"
        val = (title,)
        mycursor.execute(sql, val)  # Execute the SQL query with the title
        results = mycursor.fetchall()  # Fetch all matching rows

        if not results:
            # Raise an error if no books are found
            raise ValueError(f"No books found with title: {title}")

        # Print book details for each matching result
        for books in results:
            print(f"ID: {books[0]}, Title: {books[1]}, Author: {books[2]}, ISBN: {books[3]}")
    
    # Handle case where no books match the query
    except ValueError as e:
        print(f"Error: {e}")

    # Catch any other unexpected errors
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    # Always close cursor and connection, whether an error occurs or not
    finally:
        mycursor.close()
        mydb.close()
        print("Connection closed")

# Lists all books currently stored in the 'Books' table
def list_all_book():
    mydb = connect_to_db()  # Connect to the database
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Books")  # Execute the SQL query
    result = mycursor.fetchall()  # Fetch all rows from the 'Books' table
    
    try:
        # If rows are present, print each book's details
        if result:
            for books in result:
                print(f"ID: {books[0]}, Title: {books[1]}, Author: {books[2]}, ISBN: {books[3]}")
        else:
            # Raise an exception if no rows are found
            raise Exception
    except Exception as e:
        print(f"Error: the rows are empty")
    
    # Close cursor and connection after operation
    finally:
        mycursor.close()
        mydb.close()
        print("Connection terminated")

# Deletes a book from the 'Books' table based on the provided book ID
def delete(book_id):
    mydb = connect_to_db()  # Connect to the database
    mycursor = mydb.cursor()

    sql = "DELETE FROM Books WHERE id = %s"
    val = (book_id,)
    mycursor.execute(sql, val)  # Execute the delete query with the book ID

    mydb.commit()  # Commit changes to the database
    print(f"Row with ID {book_id} deleted successfully.")

    # Close cursor and connection
    mycursor.close()
    mydb.close()

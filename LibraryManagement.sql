CREATE DATABASE IF NOT EXISTS library_management;

-- Switches to the 'library_management' database for subsequent operations
USE library_management;

-- Creates the 'Books' table only if it doesn't already exist
CREATE TABLE IF NOT EXISTS Books (
    id INT AUTO_INCREMENT PRIMARY KEY,    -- 'id' is an integer, auto-incremented, and acts as the primary key
    title VARCHAR(255),                   -- 'title' stores the book's title, allowing up to 255 characters
    author VARCHAR(255),                  -- 'author' stores the author's name, allowing up to 255 characters
    ISBN VARCHAR(255)                     -- 'ISBN' stores the book's ISBN, allowing up to 255 characters
);

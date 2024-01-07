import sqlite3

# create .db file or connect to it if it exists
conn = sqlite3.connect("database.db")

# A cursor is an object used to make the connection for executing SQL queries.
c = conn.cursor()


# USERS TABLE
create_table_statement = """CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    dob DATE,
    fname VARCHAR(20),
    lname VARCHAR(30),
    password VARCHAR(30)
);"""
c.execute(create_table_statement)


# MOVIES TABLE
create_table_statement = """CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    title VARCHAR(20),
    release_year INTEGER
);"""
c.execute(create_table_statement)


# RATINGS TABLE (ratings are out of 5, but half-stars are allowed, e.g. 3.5)
create_table_statement = """CREATE TABLE IF NOT EXISTS ratings (
    movie_id INTEGER,
    user_id INTEGER,
    rating REAL,
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY(user_id) REFERENCES users(user)
);"""
c.execute(create_table_statement)


conn.commit()  # important! commit moves it from RAM to storage
conn.close()

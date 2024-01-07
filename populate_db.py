import sqlite3

# create DB file or connect if it exists
conn = sqlite3.connect("database.db")
c = conn.cursor()

# ----------------------------------------
# CREATE DEMO USERS AND INSERT INTO DB
# create list of demo user data and then loop over it inserting each one
demo_users = [
	["Bat","Man","password123"],
	["Wonder","Woman","321password"],
	["The","Spot","p4ssw0rd"], ]


# Loop over list of demo users, inserting each one into database
for user in demo_users:
	insert_user_statement = f"""INSERT INTO users (fname, lname, password) VALUES ('{user[0]}', '{user[1]}', '{user[2]}');"""
	c.execute(insert_user_statement)


# ----------------------------------------
# CREATE DEMO MOVIES AND INSERT INTO DB
demo_movies = [
	["Titanic",1997],
	["The Matrix",1999],
	["Into The Wild",2007],
	["Snakes on a Plane",2006],
	["Dune",1984],
	["Dune",2021]
]
for movie in demo_movies:
	insert_movie_statement = f"""INSERT INTO movies (title, release_year) VALUES ('{movie[0]}', {movie[1]});"""
	c.execute(insert_movie_statement)


# ----------------------------------------
# CREATE DEMO RATINGS AND INSERT INTO DB
# movie_id, user_id, rating

# Note this only works if you know the user_id and movie_id in advance, so it's an unnatural thing to do.
# Normally a user and a list of movies would exist first, and the user would choose to rate an already-existing movie.

demo_ratings = [
	[1,1,4], # Titanic by Bat Man
	[2,1,3.5], # The Matrix by Bat Man
	[3,1,3], # Into The Wild by Bat Man
	[4,1,2], # Snakes on a Plane by Bat Man
	[5,1,2], # Dune 1984 by Bat Man
	[6,1,4], # Dune 2021 by Bat Man
	[1,2,5], # Titanic by Wonder Woman
	[2,2,5], # The Matrix by Wonder Woman
	[3,2,4.5], # Into The Wild by Wonder Woman
	[4,2,1], # Snakes on a Plane by Wonder Woman
	[5,2,3], # Dune 1984 by Wonder Woman
	[6,2,3.5], # Dune 2021 by Wonder Woman
	[1,3,1.5], # Titanic by The Spot
	[2,3,3], # The Matrix by The Spot
	[3,3,2], # Into The Wild by The Spot
	[4,3,5], # Snakes on a Plane by The Spot
	[5,3,4.5], # Dune 1984 by The Spot
	[6,3,4.5]  # Dune 2021 by The Spot
]
for rating in demo_ratings:
	insert_rating_statement = f"""INSERT INTO ratings (movie_id, user_id, rating) VALUES ({rating[0]}, {rating[1]}, {rating[2]});"""
	c.execute(insert_rating_statement)

conn.commit()  # important! commit moves it from RAM to storage

# Remember to close connection
conn.close()

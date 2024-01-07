import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()


def printAllRows(table_name):
    c.execute(f"SELECT * FROM {table_name}")
    result = c.fetchall()
    print(f"Okay, here are all the {table_name}.")
    print()
    for r in result:
        print(r)


def runTestQuery():
    while True:
        print("\nInput your SQL query, or type 0 to cancel:")
        query = input("> ")
        if query == "0":
            print("Okay, returning to menu.")
            return
        try:  # If invalid, tries again - if not, breaks and commits
            c.execute(query)
            break
        except:
            print("Invalid query. Please try again.")
    conn.commit()
    print("Done.")


def displayAllRatingsForMovie():
    query = "select movie_id, title from movies"
    c.execute(query)
    result = c.fetchall()
    for r in result:
        print(f"{r[0]}.\t{r[1]}")

    while True:
        print("\nChoose a movie by its number to see all ratings made about that film.")
        filmNo = input("> ")
        try:
            if int(filmNo) < 1 or int(filmNo) > len(result):
                print("Out of range. Please try again")
            else:
                break
        except:
            print("Invalid film number. Please try again.")

    filmNo = int(filmNo)
    filmTitle = result[filmNo-1][1]

    query = f"""select ratings.rating, users.fname, users.lname from ratings 
                inner join users on ratings.user_id = users.user_id
                inner join movies on ratings.movie_id = movies.movie_id
                where ratings.movie_id = {filmNo}"""
    c.execute(query)
    result = c.fetchall()
    print(result)

    if str(result) != "[]":  # Checks whether there are any ratings to print from
        print(f"Here are all the ratings for {filmTitle}")
        total = 0
        for res in result:
            total += float(res[0])
            print(f"{res[1]} {res[2]}: {res[0]} stars")
        print(f"Average rating: {round(total/len(result), 2)}")
    else:
        print("This film has no ratings.")


def displayAllRatingsForUser():
    print("\nHere is the current list of users.")
    query = "select user_id, fname, lname from users"
    c.execute(query)
    result = c.fetchall()
    for r in result:
        print(f"{r[0]}.\t{r[1]} {r[2]}")

    while True:
        print("\nChoose a user by their number to see all ratings made by that user.")
        userNo = input("> ")
        try:
            if int(userNo) < 1 or int(userNo) > len(result):
                print("Out of range. Please try again")
            else:
                break
        except:
            print("Invalid user number. Please try again")

    userNo = int(userNo)
    userName = result[userNo-1][1] + " " + result[userNo-1][2]

    query = f"""select movies.title, ratings.rating from ratings
                inner join movies on ratings.movie_id = movies.movie_id
                where ratings.user_id = {userNo}"""
    c.execute(query)
    result = c.fetchall()

    if str(result) != "[]":  # Checks whether there are any ratings to print from
        print(f"Here are all of {userName}'s ratings.")
        for res in result:
            print(f"{res[0]} - {res[1]} stars")
    else:
        print("This user has no ratings.")


def addUsers():
    print("Okay, let's add some more users. Here is the current list:")
    c.execute("SELECT fname, lname from users")
    result = c.fetchall()
    for r in result:
        print(f"{r[0]} {r[1]}")

    while True:
        try:
            for i in range(int(input("How many users would you like to add? (Must be a number, type 0 to cancel): "))):
                firstname = input(f"User {i + 1}'s first name: ")
                lastname = input(f"User {i + 1}'s last name: ")
                password = input(f"User {i + 1}'s password: ")
                confirm_password = input(f"Confirm User {i + 1}'s password: ")
                while password != confirm_password:
                    print("Passwords do not match. Try again.")
                    password = input(f"User {i + 1}'s password: ")
                    confirm_password = input(f"Confirm User {i + 1}'s password: ")
                confirm = input(f"Ready to enter the following: {firstname}, {lastname}, {password}? (y/n) ")
                if confirm.upper() == "Y":
                    c.execute(f"""INSERT INTO users (fname, lname, password) 
                                  VALUES ("{firstname}", "{lastname}", "{password}")""")
                    conn.commit()
                    print("Entered.")
                    break
                print("Okay, let's try again.")
            break
        except:
            print("Invalid number. Please try again.")


def addMovies():
    print("Okay, let's add some more movies. Here is the current list:")
    c.execute("SELECT movie_id, title, release_year from movies")
    result = c.fetchall()
    for r in result:
        print(f"{r[0]}. {r[1]} ({r[2]})")

    while True:
        try:
            for i in range(int(input("How many movies would you like to add? (Must be a number, type 0 to cancel): "))):
                title = input(f"Movie {i+1}'s title: ")
                year = input(f"Movie {i+1}'s release year: ")
                confirm = input(f"Ready to enter the following: {title}, {year}? (y/n) ")
                if confirm.upper() == "Y":
                    c.execute(
                        f"""INSERT INTO movies (title, release_year) VALUES ("{title}", "{year}")""")
                    conn.commit()
                    print("Entered.")
                    break
                print("Okay, let's try again.")
            break
        except:
            print("Invalid number. Please try again.")


def addRatings():
    print("Okay, let's add some more ratings. Here is the current list of users:")
    c.execute("SELECT user_id, fname, lname from users")
    result = c.fetchall()
    for r in result:
        print(f"{r[0]}. {r[1]} {r[2]}")

    while True:
        print("\nPlease pick a user number to add rating(s) for, or type 0 to cancel. ")
        user = input("> ")
        if user == "0":
            print("Okay, returning to menu.")
            return
        else:
            try:
                if int(user) < 1 or int(user) > len(result):
                    print("Out of range. Please try again")
                else:
                    break
            except:
                print("Invalid user number. Please try again")

    reviewer = result[int(user) - 1][1] + " " + result[int(user) - 1][2]

    while True:
        # PASSWORD CHECK
        print(f"Please enter {reviewer}'s password. Leave blank to cancel.")
        password = input("> ")
        c.execute(f"SELECT password FROM users where user_id = {user}")
        correct_password = c.fetchall()[0][0]
        if password == "":
            print("Okay, returning to menu.")
            return
        if password != correct_password:
            print("Incorrect password. Try again.")
        else:
            break

    print("Here are all the movies to choose from.")
    c.execute("SELECT movie_id, title, release_year from movies")
    result = c.fetchall()
    for r in result:
        print(f"{r[0]}. {r[1]} ({r[2]})")

    while True:
        try:
            for i in range(int(input(f"""How many ratings would you like to add for {reviewer}? (Must be a number, type 0 to cancel): """))):
                movieid = input(f"Number of movie for rating {i+1}: ")
                rating = input(f"Number of stars for rating {i+1} (can have half stars): ")
                c.execute(f"SELECT title from movies where movie_id = {movieid}")
                title = c.fetchall()[0][0]
                confirm = input(f"Ready to enter the following: {reviewer}, {title}, {rating} stars? (y/n) ")
                if confirm.upper() == "Y":
                    c.execute(
                        f"""INSERT INTO ratings (movie_id, user_id, rating) VALUES ("{movieid}", "{user}", "{rating}")""")
                    conn.commit()
                    print("Entered.")
                    break
            break
        except:
            print("Invalid number. Please try again.")


while True:
    options = """ 
What would you like to do?
1. View all users
2. View all movies
3. View all ratings (raw data)
4. Run an SQL query on the database
5. View all ratings for a given film
6. View all ratings for a given user
7. Add more users
8. Add more movies
9. Add more ratings"""
    print(options)
    inp = input("> ")
    if inp == "1":
        printAllRows("users")
    elif inp == "2":
        printAllRows("movies")
    elif inp == "3":
        printAllRows("ratings")
    elif inp == "4":
        runTestQuery()
    elif inp == "5":
        displayAllRatingsForMovie()
    elif inp == "6":
        displayAllRatingsForUser()
    elif inp == "7":
        addUsers()
    elif inp == "8":
        addMovies()
    elif inp == "9":
        addRatings()
    else:
        print("Invalid choice, please try again.")
    print("\n---------------\n")

A simple command-line interface using SQL to interact with a users/movies/ratings database.  

  
![image](https://github.com/thomaswatkin1/SQLite-Movies/assets/143748754/e2494553-ac82-40d8-b153-2b83791f1684)


# Final testing:

1. View All Users - WORKING, no further testing needed
2. View All Movies - WORKING, no further testing needed
3. View All Ratings (raw) - WORKING, no further testing needed
4. Enter SQL Query - WORKING, loops (as expected) if invalid SQL entered
5. View ratings for Specific Film - WORKING, loops (expected) if boundary entered, loops (as expected) if erroneous type (e.g. a word) entered, loops (as expected) if too high
6. View ratings for Specific User - WORKING, loops (as expected) if boundary entered, loops (as expected) if erroneous type (e.g. a word) entered, loops (as expected) if too high, loops (as expected) if too high
7. Add Users - WORKING, loops (as expected) if erroneous type (e.g. a word) entered, returns to menu if '0' entered, returns to menu if user selects 'not ready to enter'
8. Add Movies - WORKING, loops (as expected) if erroneous type (e.g. a word) entered, returns to menu if '0' entered, returns to menu if user selects 'not ready to enter'
9. Add Ratings - WORKING, loops (as expected) if erroneous type (e.g. a word) entered, returns to menu if '0' entered, loops (as expected) if user number too high, loops if incorrect password entered, returns to menu if password blank, returns to menu if '0' entered, returns to menu if user selects 'not ready to enter'.

#  About the Events Database Project

The Events Database Projects is seperated 5 different files, `events.py` the main file where the database, and all the tables with their columns are created with the help of `createTable()` function. `data_values.py` is used to store all the data generated from ChatGPT into variables for each table. To store all the data into tables we use `insertValues()` function, which is called in the `eventValues.py`, followed by `eventsSolutions.py` and `eventsProcedures.py` who holds all the queries exercises

## How to run the project

First step of the project is to go to to the `events.py` file and run all the `createTable`
functions. P.s, since the database is created you might run into an error, but it is okay you can see the database and its tables for yourself via `DB Browser for SQLite`. 

## How to insert values

The values for this database project are generated from ChatGPT, and it is just dummy data, so the data does not hold any credibility whatsoever. These data are stored in seperate variables in the `data_values.py` and `data.txt` as required from the project. After checking the data you can run the `insertValues()` function through `eventValues.py`.

Again you can use `DB Browser for SQLite` to check whether the data is there, but you can also run queries from `Python` to check the data.

## Queries and Procedures Solutions

In the `eventsSolutions.py` you can find all the queries solutions in seperate variables. If you want to run any query and get all the data from it, just write `cur.execute(solution_variable)`, after that you might want to store `cur.fetchall()` into a variable of your choice and then run `print(fetching_variable)`. The code you want to write might look something like this:

`cur.execute(solution_variable)`\
`fetched_data = cur.fetchall()`\
`print(fetched_data)`

Even though, creating `PROCEDURE` in SQLite is not possible, you can achieve the same output by using `Python`. In the `eventsProcedures.py` file, you can find 2 functions created for the 2 procedures needed in this task:

`getEventByDateRange(start_date, end_date)` functions: 2 string parameters which you need to input 2 dates in the format of 'YYYY-MM-DD', then the function selects all the events which will take place in between of this date range.

`eventsOnVenue(venue_id)` function: 1 integer parameter called `venue_id`, and based on this parameter, the function will fetch all the events which will be held in that venue along with the event details. 

##    Edge Cases and Error Handling
1. Unique Identifiers for the tables is handled by using Primary Key and Autoincrement.
2. Invalid Inputs - Foreign Keys, SQL will reject invalid inputs automatically.
3. Handle Errors -  incldued in `createTable()` function with exception handling.
4. Validate details - Using `CHECK` constraints, every detail should pass the condition, before going into the table.

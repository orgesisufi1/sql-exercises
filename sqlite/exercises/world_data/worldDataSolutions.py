import sqlite3 as sq
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'world_data.db')

database_path = filename


con = sq.connect(database_path)
cur = con.cursor()


#Basic SELECT Query Task: Retrieve all columns for the top 5 countries with the highest population in 2022.
s1 = cur.execute("""
    SELECT * FROM world_data
    ORDER BY "2022Population" DESC
    LIMIT 5
""")

#Filtering Data Task: Retrieve the countries and their capitals from the continent 'Asia'.
s2 = cur.execute("""
    SELECT CountryTerritory, Capital 
    FROM world_data
    WHERE Continent = "Asia"
""")

#Sorting Data Task: List the top 7 countries by population in 2020, sorted in descending order.
s3 = cur.execute("""
    SELECT CountryTerritory FROM world_data
    ORDER BY "2022Population" DESC
    LIMIT 7
""")

#Aggregate Function Task: Find the total population of all countries in the continent 'Africa' in 2022.
s4 = cur.execute("""
    SELECT SUM("2022Population") FROM world_data
    WHERE Continent = "Africa" 
""")

#Using WHERE Clause Task: Retrieve the countries that have a population density greater than 1000 people per square kilometer.
s5 = cur.execute("""
    SELECT CountryTerritory FROM world_data
    WHERE Density >1000
""")

#Using LIKE Operator Task: Find all countries whose name starts with the letter 'A'.
s6 = cur.execute("""
    SELECT CountryTerritory FROM world_data
    WHERE CountryTerritory like 'A%'
""")

#Using BETWEEN Operator Task: Retrieve countries that had a population between 10 million and 50 million in 2000.
s7 = cur.execute("""
    SELECT CountryTerritory FROM world_data
    WHERE "2000Population" BETWEEN '10000000' AND '50000000'
""")

#Creating Views Task: Create a view that shows the country name, continent, and population in 2022 for all countries in 'Europe'.
s8 = cur.execute("""
    SELECT CountryTerritory, Continent, "2022Population" FROM world_data
    WHERE Continent = "Europe"
""")

#Updating Data Task: Update the capital of the country with CCA3 code 'USA' to 'Washington DC'.
s9 = cur.execute("""
    UPDATE world_data
    SET Capital = "Washington DC" 
    WHERE CCA3= "USA"
""")

#Deleting Data Task: Delete the data for the country with the smallest population in 2022.
s10 = cur.execute("""
    DELETE FROM world_data
    WHERE "2022Population" = (
    SELECT "2022Population" 
    FROM world_data
    ORDER BY "2022Population" ASC
    LIMIT 1
    );
""")

#Grouping Data Task: Group the countries by continent and calculate the average population in 2022 for each continent.
s11 = cur.execute("""
    SELECT AVG("2022Population"), Continent FROM world_data
    GROUP BY Continent
""")


#↓↓↓↓↓↓↓ SOLUTIONS TO ALL 11 EXERCISES ↓↓↓↓↓↓↓↓

print(s1.fetchall())
# print(s2.fetchall())
# print(s3.fetchall())
# print(s4.fetchall())
# print(s5.fetchall())
# print(s6.fetchall())
# print(s7.fetchall())
# print(s8.fetchall())
# print(s9.fetchall())
# print(s10.fetchall())
# print(s11.fetchall())

con.commit()
con.close()
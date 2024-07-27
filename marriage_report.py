import sqlite3
from faker import Faker

# Connect to the database
con = sqlite3.connect('social_network.db')
cur = con.cursor()

# SQL query to create the people table
create_people_tbl_query = """
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
"""

# Execute the SQL query
cur.execute(create_people_tbl_query)

# Prepare to populate the table with fake data
fake = Faker()
add_person_query = """
    INSERT INTO people (name) VALUES (?);
"""

# Insert 200 fake people
for _ in range(200):
    cur.execute(add_person_query, (fake.name(),))

# Commit changes and close connection
con.commit()
con.close()

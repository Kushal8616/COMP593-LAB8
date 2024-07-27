"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from random import randint, choice
from faker import Faker

# Connect to the database
con = sqlite3.connect('social_network.db')
cur = con.cursor()

# SQL query to create the relationships table
create_relationships_tbl_query = """
    CREATE TABLE IF NOT EXISTS relationships (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
    );
"""

# Execute the SQL query
cur.execute(create_relationships_tbl_query)

# Prepare to populate the table with fake data
fake = Faker()
add_relationship_query = """
    INSERT INTO relationships (
        person1_id,
        person2_id,
        type,
        start_date
    ) VALUES (?, ?, ?, ?);
"""

# Insert 100 fake relationships
for _ in range(100):
    person1_id = randint(1, 200)
    person2_id = randint(1, 200)
    while person2_id == person1_id:
        person2_id = randint(1, 200)
    rel_type = choice(['friend', 'spouse', 'partner', 'relative'])
    start_date = fake.date_between(start_date='-50y', end_date='today')
    cur.execute(add_relationship_query, (person1_id, person2_id, rel_type, start_date))

# Commit changes and close connection
con.commit()
con.close()


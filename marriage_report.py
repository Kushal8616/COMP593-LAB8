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


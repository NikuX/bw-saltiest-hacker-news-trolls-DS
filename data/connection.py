'''Includes the information and connections for connecting to ElephantSQL
database. ElephantSQL will most likely not be used for the MVP,
but will be used to get a basic database up for machine learning engineers.'''

# Imports
import psycopg2

# Connection information
dbname = 'mrbekufe'
user = 'mrbekufe'
password = '<password>'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

'''Creates a table for 'comments' table.
Columns match original Kaggle columnsfrom 'comments' table.'''
comments_table = '''
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER,
    by TEXT,
    author TEXT,
    time INTEGER,
    time_ts TEXT,
    text TEXT,
    parent INTEGER,
    deleted BOOLEAN,
    dead BOOLEAN,
    ranking INTEGER
);
'''

pg_curs.execute(comments_table)

'''Creates a table for 'full_table' table.
Columns match original Kaggle columns for 'full' table.'''
full_table = '''
CREATE TABLE IF NOT EXISTS full_table (
    by TEXT,
    score INTEGER,
    time INTEGER,
    timestamp TIMESTAMP,
    title TEXT,
    type TEXT,
    url TEXT,
    text TEXT,
    parent INTEGER,
    deleted BOOLEAN,
    dead BOOLEAN,
    descendants INTEGER,
    id INTEGER,
    ranking INTEGER
);
'''

pg_curs.execute(full_table)

'''Creates a table for 'full201510' table.
Columns match original Kaggle columns for 'full201510' table.'''

full201510_table = '''
CREATE TABLE IF NOT EXISTS full201510 (
    by TEXT,
    score INTEGER,
    time INTEGER,
    title TEXT,
    type TEXT,
    url TEXT,
    text TEXT,
    parent INTEGER,
    deleted BOOLEAN,
    dead BOOLEAN,
    descendants INTEGER,
    id INTEGER,
    ranking INTEGER
);
'''

pg_curs.execute(full201510_table)

'''Creates a table for 'stories' table.
Columns match original Kaggle columns for 'stories' table.'''

stories_table = '''
CREATE TABLE IF NOT EXISTS stories (
    id INTEGER,
    by TEXT,
    score INTEGER,
    time INTEGER,
    time_ts TEXT,
    title TEXT,
    url TEXT,
    text TEXT,
    deleted BOOLEAN,
    dead BOOLEAN,
    descendants INTEGER,
    author TEXT
);
'''

pg_curs.execute(stories_table)

# Commit the changes
pg_conn.commit()

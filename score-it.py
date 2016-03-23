# score-it.py -- score keeper app

import psycopg2
import sys

def connect():
    """Connect to the PostgreSQL database score_it.  Returns a database connection
    and a cursor object and raises eceptions if the connection cannot be made.
    """
    try:
        conn = psycopg2.connect("dbname = score_it")
    except psycopg2.DatabaseError:
        print "The program could not connect to the database!"
        sys.exit(1)
    except psycopg2.InterfaceError:
        print ("The program could not connect to the database because of "\
               "a connection.")
        sys.exit(1)
    else:
        cursor = conn.cursor()
        return conn, cursor


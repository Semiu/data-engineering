import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries, analytics_queries

# Function to execute the copy_table_queries
def load_staging_tables(cur, conn):
    """
    This function executes the queries in the copy_table_queries 
    imported from sql_queries scripts
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

# Function to execute the insert_table_queries
def insert_tables(cur, conn):
    """
    This function executes the queries in the insert_table_queries 
    imported from sql_queries scripts
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

# Function to execute the analytics_queries
def analyze_data(cur, conn):
    """
    This function executes the queries in the analytics_queries 
    imported from sql_queries scripts
    """
    for query in analytics_queries:
        cur.execute(query)
        conn.commit()

def main():
    # Initialize a config parser class method to read the .cfg file
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # connect to the database
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    # Each of the defined functions are called
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    analyze_data(cur, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()

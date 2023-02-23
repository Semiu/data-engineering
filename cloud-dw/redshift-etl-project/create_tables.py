import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    This function executes the queries in the drop_table_queries 
    imported from sql_queries scripts
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    This function executes the queries in the create_table_queries 
    imported from sql_queries scripts
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    # Initialize a config parser class method to read the .cfg file
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    # connect to the database
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    # Call the defined functions
    drop_tables(cur, conn)
    create_tables(cur, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()

import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries, analytics_queries


# Function to execute the copy_table_queries
def load_staging_tables(cur, conn):
    """
    Execute the copy_table_queries imported from sql_queries scripts
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


# Function to execute the insert_table_queries
def insert_tables(cur, conn):
    """
    Executes the insert_table_queries imported from sql_queries scripts
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


# Function to execute the analytics_queries
def analyze_data(cur, conn):
    """
    Executes the analytics_queries imported from sql_queries scripts
    """
    for query in analytics_queries:
        print(f"******Analytics Query*****")
        cur.execute(query)
        row = cur.fetchone()
        while row:
            print(row)
            row = cur.fetchone()
        conn.commit()


def main():
    # Initialize a config parser class method to read the .cfg file
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    # connect to the database
    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["CLUSTER"].values()
        )
    )
    cur = conn.cursor()

    # Each of the defined functions are called
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)
    analyze_data(cur, conn)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    main()

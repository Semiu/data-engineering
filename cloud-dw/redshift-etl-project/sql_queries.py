import configparser

# CONFIG - Read the configuration file
config = configparser.ConfigParser()
config.read('dwh.cfg')

# GET CONFIG PARAMETERS 
ARN = config.get("IAM_ROLE","ARN") # ARN Role

LOG_DATA = config.get("S3","LOG_DATA") # Log data
LOG_JSONPATH = config.get("S3","LOG_JSONPATH") # Log JSON path
SONG_DATA = config.get("S3","SONG_DATA") # Song Data

# DROP TABLES - Queries to drop each of the tables created, if exists
staging_events_table_drop = "DROP TABLE IF EXISTS 'staging_events_table';"
staging_songs_table_drop = "DROP TABLE IF EXISTS 'staging_songs_table';"
songplay_table_drop = "DROP TABLE IF EXISTS 'songplay_table';"
user_table_drop = "DROP TABLE IF EXISTS 'user_table';"
song_table_drop = "DROP TABLE IF EXISTS 'song_table';"
artist_table_drop = "DROP TABLE IF EXISTS 'artist_table';"
time_table_drop = "DROP TABLE IF EXISTS 'time_table';"

# CREATE TABLES
# Staging tables
staging_events_table_create= ("""
""")

staging_songs_table_create = ("""
""")

# Fact table
songplay_table_create = ("""
""")

# Dimension tables
user_table_create = ("""
""")

song_table_create = ("""
""")

artist_table_create = ("""
""")

time_table_create = ("""
""")

# STAGING TABLES - Copy from the designated s3 bucket to their respective staging tables
staging_events_copy = ("""copy staging_events_table from '{}' credentials 'aws_iam_role={}' region 'us-west-2';
""").format(LOG_DATA, ARN)

staging_songs_copy = ("""copy staging_songs_table from '{}' credentials 'aws_iam_role={}' region 'us-west-2';
""").format(SONG_DATA, ARN)

# FINAL TABLES - SQL to SQL ELT, selecting from the staging tables to designated fact and dimension tables
songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]

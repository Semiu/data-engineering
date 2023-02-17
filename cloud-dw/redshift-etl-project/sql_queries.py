# Import the needed library
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
CREATE TABLE "staging_events_table" (
    "event_table_id" IDENTITY(0,1) PRIMARY KEY,
    "artist" VARCHAR(50),
    "auth" VARCHAR(10) NOT NULL,
    "firstName" VARCHAR(19) NOT NULL,
    "gender" VARCHAR(5) NOT NULL,
    "itemInSession" SMALLINT NOT NULL,
    "lastName" VARCHAR(15) NOT NULL,
    "length" DECIMAL (7,5),
    "level" VARCHAR(5) NOT NULL,
    "location" VARCHAR(50) NOT NULL,
    "method" VARCHAR(5) NOT NULL,
    "page" VARCHAR(10) NOT NULL,
    "registration" BIGINT NOT NULL,
    "sessionid" INTEGER NOT NULL,
    "song" VARCHAR(100),
    "status" INTEGER NOT NULL,
    "ts" TIMESTAMP NOT NULL,
    "userAgent" VARCHAR(100) NOT NULL,
    "userId" INTEGER NOT NULL
);
""")

staging_songs_table_create = ("""
CREATE TABLE "staging_songs_table" (
    "song_table_id" IDENTITY(0,1) PRIMARY KEY,
    "num_songs" SMALLINT NOT NULL,
    "artist_id" VARCHAR(25) NOT NULL,
    "artist_latitude" DOUBLE PRECISION,
    "artist_longitude" DOUBLE PRECISION,
    "artist_location" VARCHAR(25),
    "artist_name" VARCHAR(25) NOT NULL,
    "song_id" VARCHAR(25) NOT NULL,
    "title" VARCHAR(25) NOT NULL,
    "duration" DECIMAL (7,5),
    "year" INTEGER NOT NULL
);
""")

# Fact table
# songplay_table
songplay_table_create = ("""
CREATE TABLE "songplay_table" (
    "songplay_id" IDENTITY(0,1) INTEGER NOT NULL,
    "start_time" TIME NOT NULL, 
    "user_id" INTEGER NOT NULL,
    "level"  VARCHAR(5) NOT NULL,
    "song_id" VARCHAR(25) NOT NULL,
    "artist_id" VARCHAR(25) NOT NULL,
    "session_id" INTEGER NOT NULL,
    "location" VARCHAR(25) NOT NULL,
    "user_agent" VARCHAR(100) NOT NULL
);
""")

# Dimension tables
# user table
user_table_create = ("""
CREATE TABLE "user_table" (
    "user_id" INTEGER NOT NULL,
    "first_name" VARCHAR(19) NOT NULL,
    "last_name" VARCHAR(15) NOT NULL,
    "gender" VARCHAR(5) NOT NULL,
    "level" VARCHAR(5) NOT NULL
);
""")

# song_table
song_table_create = ("""
CREATE TABLE "song_table" (
    "song_id" VARCHAR(25) NOT NULL,
    "title" VARCHAR(25) NOT NULL,
    "artist_id" VARCHAR(25) NOT NULL,
    "year"  INTEGER NOT NULL,
    "duration" DECIMAL (7,5)
);
""")

# artist_table
artist_table_create = ("""
CREATE TABLE "artist_table" (
    "artist_id" VARCHAR(25) NOT NULL,
    "artist_name" VARCHAR(25) NOT NULL,
    "artist_location" VARCHAR(25),
    "artist_latitude" DOUBLE PRECISION,
    "artist_longitude" DOUBLE PRECISION
);
""")

# time_table
time_table_create = ("""
CREATE TABLE "time_table" (
    "timestamp_id" TIMESTAMP NOT NULL,
    "start_time" TIME NOT NULL,
    "hour" TIME NOT NULL,
    "day" TIME NOT NULL,
    "week" TIME NOT NULL,
    "month" TIME NOT NULL,
    "year" TIME NOT NULL,
    "weekday" TIME NOT NULL
    
);
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

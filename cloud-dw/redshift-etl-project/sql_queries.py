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
staging_events_table_drop = """DROP TABLE IF EXISTS staging_events_table;"""
staging_songs_table_drop = """DROP TABLE IF EXISTS staging_songs_table;"""
songplay_table_drop = """DROP TABLE IF EXISTS songplay_table;"""
user_table_drop = """DROP TABLE IF EXISTS user_table;"""
song_table_drop = """DROP TABLE IF EXISTS song_table;"""
artist_table_drop = """DROP TABLE IF EXISTS artist_table;"""
time_table_drop = """DROP TABLE IF EXISTS time_table;"""

# CREATE TABLES
# Staging tables
staging_events_table_create= ("""
CREATE TABLE staging_events_table (
    "event_table_id" INT IDENTITY(0,1),
    "artist" VARCHAR(65535),
    "auth" TEXT,
    "firstName" TEXT,
    "gender" TEXT,
    "itemInSession" SMALLINT,
    "lastName" TEXT,
    "length" DECIMAL(13,2),
    "level" TEXT,
    "location" TEXT,
    "method" TEXT,
    "page" TEXT,
    "registration" BIGINT,
    "sessionid" INTEGER,
    "song" TEXT,
    "status" INTEGER,
    "ts" BIGINT,
    "userAgent" VARCHAR(65535),
    "userId" INTEGER
);
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs_table (
    "song_table_id" INT IDENTITY(0,1),
    "num_songs" SMALLINT,
    "artist_id" VARCHAR(65535),
    "artist_latitude" DOUBLE PRECISION,
    "artist_longitude" DOUBLE PRECISION,
    "artist_location" TEXT,
    "artist_name" VARCHAR(65535),
    "song_id" TEXT,
    "title" VARCHAR(65535),
    "duration" DECIMAL(26,7),
    "year" INTEGER
);
""")

# Fact table
# songplay_table
songplay_table_create = ("""
CREATE TABLE songplay_table (
    "songplay_id" INTEGER IDENTITY(0,1),
    "start_time" TIMESTAMP, 
    "user_id" INTEGER,
    "level"  TEXT,
    "song_id" TEXT,
    "artist_id" VARCHAR(65535),
    "session_id" INTEGER,
    "location" TEXT,
    "user_agent" VARCHAR(65535)
   );
""")

# Dimension tables
# user table
user_table_create = ("""
CREATE TABLE user_table (
    "user_id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "gender" TEXT,
    "level" TEXT
);
""")

# song_table
song_table_create = ("""
CREATE TABLE song_table (
    "song_id" TEXT,
    "title" VARCHAR(65535),
    "artist_id" VARCHAR(65535),
    "year"  INTEGER,
    "duration" DECIMAL(26,7)
);
""")

# artist_table
artist_table_create = ("""
CREATE TABLE artist_table (
    "artist_id" VARCHAR(65535),
    "artist_name" VARCHAR(65535),
    "artist_location" TEXT,
    "artist_latitude" DOUBLE PRECISION,
    "artist_longitude" DOUBLE PRECISION
);
""")

# time_table
time_table_create = ("""
CREATE TABLE time_table (
    "timestamp_id" BIGINT,
    "start_time" TIMESTAMP,
    "hour" INTEGER,
    "day" INTEGER,
    "week" INTEGER,
    "month" INTEGER,
    "year" INTEGER,
    "weekday" INTEGER
    
);
""")

# STAGING TABLES - Copy from the designated s3 bucket to their respective staging tables
staging_events_copy = ("""copy staging_events_table from '{}' credentials 'aws_iam_role={}' format as JSON 'auto' region 'us-west-2';
""").format(LOG_DATA, ARN)

staging_songs_copy = ("""copy staging_songs_table from '{}' credentials 'aws_iam_role={}' format as JSON 'auto' region 'us-west-2';
""").format(SONG_DATA, ARN)

# FINAL TABLES - SQL to SQL ELT, selecting from the staging tables to designated fact and dimension tables
songplay_table_insert = ("""
INSERT INTO "songplay_table"(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
SELECT DISTINCT (timestamp 'epoch' + ts * interval '0.001 seconds') AS start_time,
    userId AS user_id, 
    ste.level, sts.song_id, sts.artist_id,
    sessionid AS session_id, ste.location,
    userAgent AS user_agent
FROM staging_events_table ste
JOIN staging_songs_table sts ON (ste.artist = sts.artist_name)
LEFT JOIN staging_songs_table stsb ON (ste.song = stsb.title);
""")

user_table_insert = ("""
INSERT INTO "user_table"(user_id, first_name, last_name, gender, level)
SELECT DISTINCT userId AS user_id,
    firstName AS first_name,
    lastName AS last_name,
    gender, level
FROM staging_events_table;
""")

song_table_insert = ("""
INSERT INTO "song_table"(song_id, title, artist_id, year, duration)
SELECT DISTINCT song_id, title, artist_id, year, duration
FROM staging_songs_table;
""")

artist_table_insert = ("""
INSERT INTO "artist_table"(artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
SELECT DISTINCT artist_id, artist_name, artist_location, artist_latitude, artist_longitude
FROM staging_songs_table;
""")

time_table_insert = ("""
INSERT INTO "time_table"(timestamp_id, start_time, hour, day, week, month, year, weekday)
SELECT DISTINCT ts AS timestamp_id, 
    (timestamp 'epoch' + ts * interval '0.001 seconds') AS start_time,
    EXTRACT(hour FROM start_time) AS hour,
    EXTRACT(day FROM start_time) AS day,
    EXTRACT(week FROM start_time) AS week,
    EXTRACT(month FROM start_time) AS month,
    EXTRACT(year FROM start_time) AS year,
    EXTRACT(weekday FROM start_time) AS weekday
FROM staging_events_table;
""")

# Analytic Queries

artists_stats = ("""
SELECT at.artist_id, artist_name, artist_location
	FROM artist_table at
    JOIN songplay_table st
    ON at.artist_id = st.artist_id LIMIT 10;
""")

songs_stats = ("""
SELECT sgt.song_id, title, sgt.artist_id, year, duration 
    FROM song_table sgt
    JOIN songplay_table st
    ON sgt.song_id = st.song_id LIMIT 10;   
""")

# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]

# These are the added analytics queries - relying on the fact-dimension schema designed
analytics_queries = [artists_stats, songs_stats]

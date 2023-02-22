## Introduction

This directory contains the cloud data warehouse project which is the second project of the Udacity Nanodegree in Data Engineering with AWS.

The project demonstrates the understanding of using AWS services, such as S3, RedShift and EC2 to implement data warehouse infrastructure for the analytics use cases of a fictitious music streaming startup.

## Schema Design

The `sql_queries.py` contains scripts that define and implement the data warehouse schema

Seven (7) tables were implemented - 2 as the staging tables and 5 as the fact-schema tables. The staging tables; `staging_events_table` and `staging_songs_table`, schema reflect the structure of the data coming from the s3 buckets, and expected to be loaded into the staging tables in Redshift.

Primary Key identity is given to these tables, following the Redshift `IDENTITY(0,1)` implementation. Respective data types are provided based on intuitive understanding of the data columns and the information about different types of data supported by Redshift. 

Though preliminary guide was provided for the fact-dimension relationship of the fact and dimension tables. Further thought was given relationship keys even though Redshift does not enforce them. In this light, the fact table has a relationship with the each of the dimension table. This would provide opportunity for aggregates and analysis. 

These five fact-dimension tables `user_table`, `songplay_table`, `song_table`, `artist_table` and `time_table` follow this pattern and the ETL SQL queries are provided to transform loaded data from the staging tables to the fact and dimension tables.

## Scripts

The create scripts which include the `CREATE` and `DROP` queries, and the `INSERT` scripts, which include the `COPY` statement and the SQL to SQL ELT queries are all in the `sql_queries.py` file. 

A section on analytics, providing descriptive information about the songs, users, and artists, is also provided. 


## How to run 

First, run `create_tables.py` script to take care of creation of the tables.

Second, run `etl.py` script for the ETL, and the added analytics queries.

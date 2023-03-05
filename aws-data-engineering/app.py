from pyspark.sql import SparkSession
import os
from util import get_spark_session
from read import from_files


def main():
    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f'{os.environ.get("SRC_DIR")}--*'
    src_file_format = os.environ.get('SRC_FILE_FORMAT')
    spark = get_spark_session(env, 'Getting started with GitHub Activity')

    df = from_files(spark,  src_dir, src_file_pattern, src_file_format)

    df.printSchema()
    df.select('repo.*').show()

    #spark.sql('SELECT current_date').show()  # Current date dataframe


if __name__ == '__main__':
    main()

# Working around
# get_spark_session()
# print(type(spark)) #Type of the spark session

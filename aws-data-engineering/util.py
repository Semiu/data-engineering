from pyspark.sql import SparkSession

#Create spark object from Spark session


def get_spark_session(env, app_name):
    if env == 'DEV':
        spark = SparkSession. \
            builder. \
            master('local'). \
            appName(app_name). \
            getOrCreate()

    return spark


#'Getting started for GitHub activity'

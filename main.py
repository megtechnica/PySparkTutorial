import pyspark

from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Practice').getOrCreate()

df_pyspark=spark.read.csv('myPracticeCSV.csv')

df_pyspark.show()

df_pyspark2=spark.read.option('header','true').csv('myPracticeCSV.csv').show()

spark=SparkSession.builder.appName('Dataframe').getOrCreate()

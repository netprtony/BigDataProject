from pyspark.sql import SparkSession

# Khởi tạo Spark session
spark = SparkSession.builder \
    .appName("Test Spark") \
    .getOrCreate()

print("Spark session created successfully!")

# Tắt Spark session
spark.stop()    
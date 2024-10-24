from pyspark.sql import SparkSession

# Tạo SparkSession
spark = SparkSession.builder \
    .appName("HadoopToMongoDB") \
    .config("spark.mongodb.input.uri", "mongodb://localhost:27017/database.Sleep") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/database.Sleep") \
    .getOrCreate()

# Đọc dữ liệu từ Hadoop (thay đổi đường dẫn đến file của bạn)
hadoop_data_path = "hdfs://localhost:9000/netprtony/14-Sleep_health_and_lifestyle_dataset.csv"
df = spark.read.csv(hadoop_data_path, header=True, inferSchema=True)

# Hiển thị dữ liệu đã đọc
df.show()

# Ghi DataFrame vào MongoDB
df.write.format("mongo").mode("append").save()

# Dừng SparkSession
spark.stop()
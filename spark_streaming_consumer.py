from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("SensorStreaming").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", DoubleType()),
    StructField("humidity", DoubleType()),
    StructField("timestamp", LongType())
])

df = spark.readStream.format("kafka").option("Kafka.bootstrap.servers", "localhost:9092").option("subscribe", "sensor_data").load()

datos = df.select(from_json(col("value").cast("string"), schema).alias("d")).select("d.*")

datos = datos.withColumn("hora", to_timestamp(from_unixtime(col("timestamp"))))

resumen = datos.groupBy(window("hora", "1 minute")).agg(avg("temperature").alias("temp_promedio"), avg("humidity").alias("humedad_promedio"))

consulta = resumen.writeStream.outputMode("update").format("console").start()
consulta.awaitTermination()

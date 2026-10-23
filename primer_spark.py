from pyspark.sql import SparkSession

spark = SparkSession.builder \
.appName("MiPrimerProyectoBigData") \
.master("local[*]") \
.getOrCreate()

print("¡Apache Spark funciona correctamente!")

datos = [(1, "Ana", 25), (2, "Carlos", 30), (3, "Laura", 22)]

columnas = ["id", "nombre", "edad"]

df = spark.createDataFrame(datos, columnas)

df.show()

spark.stop()

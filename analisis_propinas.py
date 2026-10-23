from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, round

spark = SparkSession.builder \
.appName("AnalisisPropinasRestaurantes") \
.master("local[*]") \
.getOrCreate()

archivo = "/home/matheus/Proyecto_BigData/datos/propinas.csv"

df = spark.read.csv(archivo, header=True, inferSchema=True)

print("LIMPIEZA DE DATOS")
print("Registros antes de limpiar:", df.count())

df = df.dropna()
df = df.dropDuplicates()

print("Registros despues de limpiar:", df.count())

print("DATOS ORIGINALES")
df.show(5)

print("ESTRUCTURA DE LOS DATOS")
df.printSchema()

print("CANTIDAD DE REGISTROS")

print(df.count())

print("ESTADISTICAS GENERALES")

df.select(
round(avg("total_bill"), 2).alias("Promedio_Cuenta"),
round(avg("tip"), 2).alias("Promedio_Propina"),
round(avg("size"), 2).alias("Promedio_Personas")
).show()

print("CUENTA PROMEDIO POR DIA")

df.groupBy("day").agg(
round(avg("total_bill"), 2).alias("Promedio_Cuenta")
).orderBy(col("Promedio_Cuenta").desc()).show()


spark.stop()

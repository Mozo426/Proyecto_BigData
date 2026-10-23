Proyecto Big Data: analisis por lotes y streaming

1.Descripcion

Este proyecto academico explora el procesamientode datos
mediante Apache Spark y PySpark. Incluye analisis por lotes
de un conjunto de datos de propinas y un ejercicio de
procesamiento en streaming con Apache Kafka y Spark
Structured Streaming.

2.Tecnologias utilizadas

. Python 3
. Apache Spark 3.5.0 
. PySpark 3.5.0
. Apache Kafka
. pandas/CSV como formato de datos de entrada 

3.Estructura del proyecto

.analisis_propinas.py: limpieza y analisis exploratorio
de los datos.
.datos/propinas.csv:conjunto de datos utilizado para el analisis.
.grafica_propinas.py:generacion de visualizaciones.
.grafica_cuentas.png:grafica generada por el proyecto.
.primer_spark.py:prueba inicial de PySpark
.Kafka_producer.py:productor de mensajes simulados de sensores.
.Kafka_Consumer.py:consumidor de mensajes Kafka.
.spark_streaming_consumer.py:procesamiento de mensajes mediante Spark Structured Streaming.
.resumen_resultados.txt:resumen de los resultados obtenidos.

4.Ejecucion del analisis por lotes 

Desde la carpeta del proyecto, ejecutar:

python3 analisis_propinas.py

Para generar la grafica:

python3 grafica_propinas.py


5.Ejecucion de streaming

Para probar el streaming se deben iniciar los servicios de
Kafka, ejecutar el productor de mensajes y despues iniciar el
consumidor Spark con el conector Kafka compatible con Spark
3.5.0.

spark-submit --packages org.apache.spark:spark-sql-Kafka-0-10_2.12:3.5.0 ~/Proyecto_BigData/spark_streaming_consumer.py

6.Resultados

En el analisis por lotes se trabajo con un archivo de 244
registros; despues de la limpieza se conservaron 243. El
promedio de la cuenta fue aproximadamente 19,81 y el
promedio de la propina fue aproximadamente 3,00.

En la prueba de streaming, Spark recibio mensajes simulados
de sensores y calculo promedios de temperatura y humedad
en distintos lotes de procesamiento.

7.Conclusion

La practica permitio explorar el analisis por lotes con PySpark y
el procesamiento de eventos en streaming con Kafka y Spark
Structured Streaming. Los resultados muestran como estas
herramientas permiten analizar conjuntos de datos y procesar
informacion que llega continuamente.

8.Reproducibilidad

Las rutas, dependencias y servicios deben configurarse segun
el entorno donde se ejecute el proyecto. Antes de ejecutar el
streaming, se debe commprobar que Kafka este activo y que el
productor publique mensajes en el topico esperado.



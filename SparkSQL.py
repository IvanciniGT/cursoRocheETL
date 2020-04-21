# Conexion Spark (SparkContext o SparkSession)
from pyspark import Row
from pyspark.sql import SparkSession

CPUs = 2
DIRECCION_MAESTRO_SPARK = "local["+str(CPUs)+"]"
MI_APP="AplicacionMuestra1"

sesion_spark = SparkSession.builder \
                           .master(DIRECCION_MAESTRO_SPARK) \
                           .appName(MI_APP) \
                           .getOrCreate()

# Manipulación datos
datos_originales=sesion_spark.read\
    .format('com.databricks.spark.csv')\
    .options(header='true',inferschema='true')\
    .option("sep",",")\
    .option("quote","\"")\
    .option("escape","\"")\
    .load('revisiones.csv')

datos_originales.show()
datos_originales.printSchema()

datos_originales.select("overall").show()
datos_originales.select(datos_originales['overall'], datos_originales['overall']+1).show()
total_menores_3=datos_originales.select(datos_originales['overall'], datos_originales['overall']+1)\
    .filter(datos_originales['overall'] <3).count()
print(total_menores_3)


datos_originales.groupBy("overall").count().show()

datos_originales.createOrReplaceTempView("revisiones")
sesion_spark.sql("SELECT reviewerID,asin,reviewerName,helpful FROM revisiones").show()

# Cierro conexión Spark
sesion_spark.stop()




#

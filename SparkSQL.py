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
    .load('revisiones.csv')

datos_originales.show()

# Cierro conexión Spark
sesion_spark.stop()




#

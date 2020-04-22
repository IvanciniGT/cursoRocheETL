# Conexion Spark (SparkContext o SparkSession)
from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

CPUs = 2
DIRECCION_MAESTRO_SPARK = "local["+str(CPUs)+"]"
MI_APP="AplicacionMuestra1"

sesion_spark = SparkSession.builder \
                           .master(DIRECCION_MAESTRO_SPARK) \
                           .appName(MI_APP) \
                           .getOrCreate()

VENTANA_TIEMPO=10
sesion_spark_streaming = StreamingContext(sesion_spark.sparkContext, VENTANA_TIEMPO)

# Manipulacion de datos
## RDD => Dataframes = RDD(Row)
## DStream = Coleccion RDDs

# Accede a los datos del puerto 10000
coleccion_textos=sesion_spark_streaming.socketTextStream("localhost",10000)

# Opera sobre ellos
coleccion_textos.foreachRDD(lambda textos:textos.foreach(lambda linea:print(linea)))
# Guarda en base de datos

# Iniciar la sesion
sesion_spark_streaming.start()
sesion_spark_streaming.awaitTermination()

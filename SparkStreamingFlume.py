# Conexion Spark (SparkContext o SparkSession)
from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

CPUs = 2
DIRECCION_MAESTRO_SPARK = "local["+str(CPUs)+"]"
MI_APP="AplicacionMuestra1"

sesion_spark = SparkSession.builder \
                           .master(DIRECCION_MAESTRO_SPARK) \
                           .appName(MI_APP) \
                           .getOrCreate()

VENTANA_TIEMPO=10
sesion_spark_streaming = StreamingContext(sesion_spark.sparkContext, VENTANA_TIEMPO)

# Captura de datos de flume
flumeStream = FlumeUtils.createStream(sesion_spark_streaming, "localhost", 33333)

# Procesamiento
def procesarRDD(rdd):
    print("Comenzando RDD")
    rdd.foreach(print)
    print("Acabando RDD")
flumeStream.foreachRDD(procesarRDD)

# Iniciar la sesion
sesion_spark_streaming.start()
sesion_spark_streaming.awaitTermination()

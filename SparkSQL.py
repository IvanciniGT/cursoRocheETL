# Conexion Spark (SparkContext o SparkSession)
from pyspark import Row
from pyspark.sql import SparkSession

CPUs = 2
DIRECCION_MAESTRO_SPARK = "spark://10.0.2.15:7077"
MI_APP="AplicacionMuestra1"
sesion_spark = SparkSession.builder \
                           .appName(MI_APP) \
    .master(DIRECCION_MAESTRO_SPARK) \
    .getOrCreate()

datos_originales=sesion_spark.read\
    .format('com.databricks.spark.csv')\
    .options(header='true',inferschema='true')\
    .option("sep",",")\
    .option("quote","\"")\
    .option("escape","\"")\
    .load('/home/usuario/PycharmProjects/EjemplosSpark/revisiones.csv')

datos_originales.show()
datos_originales.printSchema()


datos_originales.write.mode("append") \
        .jdbc("jdbc:mariadb://localhost:3306/curso", "mitabla1",
              properties={"user": "alumno", "password": "password"})

#
datos_leidos=sesion_spark.read \
        .jdbc("jdbc:mariadb://localhost:3306/curso", "mitabla1",
              properties={"user": "alumno", "password": "password"})

print("He leido datos de la base de datos")
datos_leidos.show()
#
# datos_originales.select("overall").show()
# datos_originales.select(datos_originales['overall'], datos_originales['overall']+1).show()
# total_menores_3=datos_originales.select(datos_originales['overall'], datos_originales['overall']+1)\
#     .filter(datos_originales['overall'] <3).count()
# print(total_menores_3)
#
#
# datos_originales.groupBy("overall").count().show()
#
# datos_originales.createOrReplaceTempView("revisiones")
# sesion_spark.sql("SELECT reviewerID,asin,reviewerName,helpful FROM revisiones").show()

sesion_spark.stop()


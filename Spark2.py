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

# Crear RDDs (conjuntos de datos) en Spark
textos=["Hola amigo","Adios amigo"]
rdd=sesion_spark.sparkContext.parallelize(textos)

# Transformaciones
# Reducción
la_palabra=rdd .map(lambda texto:texto.upper())\
    .flatMap(lambda texto:texto.split())\
    .map(lambda palabra: (palabra,1)  )\
    .reduceByKey(lambda a,b:a+b) \
    .sortBy(lambda tupla:tupla[1],ascending=False) \
    .take(1)
print(la_palabra)

textos=["Ivan Osuna 42","Ivan Diego 19","Agustin Diego Lopez 36"]
rdd=sesion_spark.sparkContext.parallelize(textos)
# Apellido: Mayusculas
# Separado Nombre, apellido y edad
# ordenado por edad de menor a mayor
import re
# def particionamientoDatos(lineaDatos):
#     particion1 = re.split(" ", lineaDatos, 1)
#     particion2 = re.split("[ ](?=[0-9])", particion1[1], 1)
#     return (particion1[0],particion2[0],int(particion2[1]))
#
# #    .repartition(1) \
# #    .sortBy(lambda datos:datos[2]) \
# rdd .map(particionamientoDatos)\
#     .map(lambda datos: (datos[0],datos[1].upper(),datos[2])) \
#     .map(lambda datos:(datos[0],1)) \
#     .reduceByKey(lambda a,b:a+b) \
#     .foreach(lambda linea:print(linea))

#rdd -> dataFrame = RDD( Row )

def particionamientoDatos(lineaDatos):
    particion1 = re.split(" ", lineaDatos, 1)
    particion2 = re.split("[ ](?=[0-9])", particion1[1], 1)
    return (particion1[0],particion2[0],particion2[1])

rdd.foreach(lambda dato:print(dato))

rdd_particionado=rdd .map(particionamientoDatos)
rdd_particionado.foreach(lambda dato: print(dato))

rdd_filas=rdd_particionado.map(lambda datos: Row(nombre=datos[0],apellidos=datos[1],edad=datos[2]))
rdd_filas.foreach(lambda dato: print(dato))

df=rdd_filas.toDF()
df.show()
#df.orderBy('edad')
df.groupBy('nombre').count().show()
df.select('apellidos','edad').orderBy('apellidos').show()
# Cierro conexión Spark
sesion_spark.stop()




#

# Conexion Spark (SparkContext o SparkSession)
from pyspark.sql import SparkSession

CPUs = 2
DIRECCION_MAESTRO_SPARK = "local["+str(CPUs)+"]"
MI_APP="AplicacionMuestra1"

sesion_spark = SparkSession.builder \
                           .master(DIRECCION_MAESTRO_SPARK) \
                           .appName(MI_APP) \
                           .getOrCreate()

# Crear RDDs (conjuntos de datos) en Spark
numeros=[1,2,3,4,5]
miRDD_numeros = sesion_spark.sparkContext.parallelize(numeros)

# Aplicar transformacionES sobre conjunto de datos RDDs
#def doblar(a):
#    return a*2

#miRDD_doblado=miRDD_numeros.map(doblar)  # [1,2,3,4,5] => [2,4,6,8,10]
miRDD_doblado=miRDD_numeros.map(lambda a:a*2)  # [1,2,3,4,5] => [2,4,6,8,10]

# Aplicar UNA funcion de reduccion sobre mis conjuntos de datos
# numeros_doblado=miRDD_doblado.collect()
# numeros_doblado_primero=miRDD_doblado.first()
# numeros_doblado_los_3_primeros=miRDD_doblado.take(3)
# numeros_doblado_suma=miRDD_doblado.sum()
# numeros_doblado_media=miRDD_doblado.mean()
# numeros_doblado_maximo=miRDD_doblado.max()
# numeros_doblado_minimo=miRDD_doblado.min()
# numeros_doblado_numero_total=miRDD_doblado.count()
# def totalizar(a,b):
#    return a+b
#total=miRDD_doblado.reduce( totalizar )
# [2,4,6,8,10]
# [ 6 ,6,8,10]
# [ 6 ,6, 18 ]
# [ 6 ,   24 ]
#     30
total=miRDD_doblado.reduce( lambda a,b : a+b )
print(total)


miRDD_numeros = sesion_spark.sparkContext.parallelize(numeros)
#[1,  2  ,  3  ,  4    ,5]
#[3,  6  ,  9  ,  12  ,15]
#[1,  0,    1,    0,   1 ] => 3
# impares = miRDD_numeros\
#              .map(lambda a:3*a) \
#              .map(lambda a:a%2) \
#              .reduce(lambda a,b:a+b) # sum()
# print(impares)
#
# pares = miRDD_numeros\
#              .map(lambda a:3*a) \
#              .map(lambda a:a%2) \
#              .filter(lambda a:a==0) \
#              .count()
# print(pares)


ordenados = miRDD_numeros\
             .map(lambda a:3*a) \
             .filter(lambda a:a%2==0) \
             .sortBy(lambda a:a,ascending=False) \
             .collect()
print(ordenados)


# // Division entera
# 5 // 2 => 2
# % Modulo: Resto de Division entera
# 5 % 2 => 1



# Cierro conexión Spark
sesion_spark.stop()

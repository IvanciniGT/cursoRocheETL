./spark-submit --master spark://10.0.2.15:7077
--driver-class-path /home/usuario/PycharmProjects/EjemplosSpark/drivers/mariadb/mariadb-java-client-2.5.4.jar
--jars /home/usuario/PycharmProjects/EjemplosSpark/drivers/mariadb/mariadb-java-client-2.5.4.jar
~/PycharmProjects/EjemplosSpark/SparkSQL.py


./spark-submit --master spark://10.0.2.15:7077 --driver-class-path /home/usuario/PycharmProjects/EjemplosSpark/drivers/mariadb/mariadb-java-client-2.5.4.jar --jars /home/usuario/PycharmProjects/EjemplosSpark/drivers/mariadb/mariadb-java-client-2.5.4.jar ~/PycharmProjects/EjemplosSpark/SparkSQL.py


./spark-submit --master spark://10.0.2.15:7077 --jars /home/usuario/PycharmProjects/EjemplosSpark/lib/spark-streaming-flume-assembly_2.11-2.4.5.jar ~/PycharmProjects/EjemplosSpark/SparkStreamingFlume.py
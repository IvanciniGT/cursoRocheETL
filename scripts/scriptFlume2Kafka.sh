

# Arranco zookeeper
cd kafka
export CLASSPATH=
bin/zookeeper-server-start.sh config/zookeeper.properties

# Arranco server kafka
bin/kafka-server-start.sh config/server.properties

# Creo topic

bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic flume2kafka

# Confirmar la creación
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Para ver que estan llegando a kafka los mensajes
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic flume2kafka --from-beginning

# creo un fichero de ejecucion del agente flume: kafka.sh

echo "flume-ng agent --name agenteKafka --conf conf --conf-file $FLUME_HOME/conf/kafka.conf -Dflume.root.logger=INFO,console" > \
   /home/usuario/flume/conf/kafka.sh

# Asigno permisos de ejecución
chmod 777 /home/usuario/flume/conf/kafka.sh

# Crear el fichero del agente kafka: kafka.conf

# Ejecuar el agent
cd /home/usuario/flume/conf
./kafka.sh

#Escribir el el fichero y ver que llega a kafka
echo "Una nueva linea... que hase" > mikafka.txt
# (En otra terminal que tenia abierta con kafka)
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic flume2kafka --from-beginning
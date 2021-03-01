#!/bin/bash

# Build project
mvn clean install

# constructing the classpath
string=":./"
total=""
for x in ./target/lib/*.jar; do
        total="${string}${x}${total}"
done

# Instantiate Master
java -cp .:./zookeeper-3.4.10/zookeeper-3.4.10.jar${total}:./target/zookeeper-1.0-SNAPSHOT.jar:./target/classes Master $1 &
sleep 3

# Instantiate workers, number of workers specified by argument
a=$2
while [ $a -gt 0 ]
do
	let "a = ${a} - 1"
	java -cp .:./zookeeper-3.4.10/zookeeper-3.4.10.jar${total}:./target/zookeeper-1.0-SNAPSHOT.jar:./target/classes Worker $1 &

done

# Instantiate Client
java -cp .:./zookeeper-3.4.10/zookeeper-3.4.10.jar${total}:./target/zookeeper-1.0-SNAPSHOT.jar:./target/classes Client $1 $3 &

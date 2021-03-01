#!/bin/bash

string=":./"
total=""
for x in ./target/lib/*.jar; do
        total="${string}${x}${total}"
done
java -cp .:./zookeeper-3.4.10/zookeeper-3.4.10.jar${total}:./target/zookeeper-1.0-SNAPSHOT.jar:./target/classes Master $1 &
sleep 3
a=$2
while [ $a -gt 0 ]
do
	let "a = ${a} - 1"
	java -cp .:./zookeeper-3.4.10/zookeeper-3.4.10.jar${total}:./target/zookeeper-1.0-SNAPSHOT.jar:./target/classes Worker $1 &

done
java -cp .:./zookeeper-3.4.10/zookeeper-3.4.10.jar${total}:./target/zookeeper-1.0-SNAPSHOT.jar:./target/classes Client $1 $3 &

#!/bin/sh
# Script to generate random traffic using the tool 
repeat=60
counter=0
while [ $counter -lt $repeat ]
do
counter=`expr $counter + 1`
echo "Test Counter : $counter"
var=`date +%M`
echo $var
cd /home/syeds/Downloads
echo "GET http://192.168.56.102:5000" | ./vegeta attack -duration=1m  -rate=$var -timeout=300s | tee reports.bin | ./vegeta report
done




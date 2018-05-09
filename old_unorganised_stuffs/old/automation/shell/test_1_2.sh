#!/usr/bin/env bash

#mkdir /extra/etc/local.d/1.ini
#docker create --net=host --volume /extra/data:/opt/couchdb/data --volume /extra/etc/local.d:/opt/couchdb/etc/local.d  couchdb:2.1.1




mkdir /home/ubuntu/couchDB/data
mkdir /home/ubuntu/couchDB/etc/
mkdir /home/ubuntu/couchDB/etc/local.d
#rm /home/ubuntu/couchDB/etc/local.d/*
echo ""
echo "Creating ini file "
touch /home/ubuntu/couchDB/etc/local.d/1.ini
echo ""

echo "changing ownership of the whole couchDB folder"
sudo chown -R ubuntu:ubuntu /home/ubuntu/couchDB
sudo chmod -R 777 /home/ubuntu/couchDB

echo "Declaring nodes, master nodes variables"
#declare nodes=(115.146.85.192 115.146.86.208)
declare nodes=(115.146.84.90 115.146.86.200 115.146.86.248)
export masternode=`echo ${nodes} | cut -f1 -d' '` #the first element in that array
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=password
echo ""

echo "Creating docker container"
docker create --net=host -p 5984:5984 --volume /home/ubuntu/couchDB/data:/opt/couchdb/data --volume /home/ubuntu/couchDB/etc/local.d:/opt/couchdb/etc/local.d  apache/couchdb:2.1.1
echo ""
echo "DOES DECLARE CONTS WORK?"
declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d"\n"`)

echo "YES"
echo ""
for cont in "${conts[@]}"; do docker start ${cont}; done

sleep 3


my_public_IP=$(curl ifconfig.me)

echo "write things to the config files"
docker exec ${conts[0]} \
bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec ${conts[0]} \
bash -c "echo \"-name couchdb@${my_public_IP}\" >> /opt/couchdb/etc/vm.args"
echo ""
echo "restart container after"
for cont in "${conts[@]}"; do docker restart ${cont}; done
sleep 3
echo ""
echo "SETTING UP ADMIN AND ADDING NODES"

curl -XPUT "http://localhost:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""

curl -XPUT "http://${user}:${pass}@localhost:5984/_node/couchdb@${my_public_IP}/_config/chttpd/bind_address" --data '"0.0.0.0"'

curl ${my_public_IP}:5984

curl -XPUT admin:password@localhost:5984/twitter

echo "yes"

declare nodes=(115.146.86.34 115.146.86.96 115.146.86.172)
export masternode=`echo ${nodes} | cut -f1 -d' '` #the first element in that array
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=password
export ending_number = 172

echo $size

echo "creating container"

docker create -p 5984:5984 --net=host apache/couchdb:2.1.1

echo "DO IT WORK?"
declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d"\n"`)

echo "YES"
for cont in "${conts[@]}"; do docker start ${cont}; done
sleep 3

echo "write things to the config files"
docker exec ${conts[0]} \
bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec ${conts[0]} \
bash -c "echo \"-name couchdb@115.146.86.172\" >> /opt/couchdb/etc/vm.args"

echo "restart container after"
for cont in "${conts[@]}"; do docker restart ${cont}; done
sleep 3

echo "DOES SETTING UP ADMIN AND ADDING NODES WORK?"

curl -XPUT "http://115.146.86.172:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""

curl -XPUT "http://${user}:${pass}@115.146.86.172:5984/_node/couchdb@115.146.86.172/_config/chttpd/bind_address" --data '"0.0.0.0"'

echo "yes"

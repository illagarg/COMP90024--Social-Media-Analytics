(declare nodes=(115.146.86.34 115.146.86.96 115.146.86.172)
export masternode=`echo ${nodes} | cut -f1 -d' '` #the first element in that array
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=password)


(nodes=(115.146.86.34 115.146.86.96 115.146.86.172)
masternode=`echo ${nodes} | cut -f1 -d' '` #the first element in that array
othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
size=${#nodes[@]}
user=admin
pass=password)

#run these on each machine curl -X POST -H "Content-Type: application/json" 
#http://admin:password@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", 
#"bind_address":"0.0.0.0", "username": "admin", "password":"password", "node_count":"3"}'
docker run -d -p 5984:5984 -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=password -v $(pwd):/opt/couchdb/data --name couchdb96  apache/couchdb:2.1.1 -net=host



docker create -v ~/data:/opt/couchdb/data -p 5984:5984 --net=host apache/couchdb:2.1.1

declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d"\n"`)



for cont in "${conts[@]}"; do docker start ${cont}; done
sleep 3



docker exec ${conts[0]} \
bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec ${conts[0]} \
bash -c "echo \"-name couchdb@115.146.86.34\" >> /opt/couchdb/etc/vm.args"

for cont in "${conts[@]}"; do docker restart ${cont}; done
sleep 3


  
curl -XPUT "http://115.146.86.34:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""    
curl -XPUT "http://${user}:${pass}@115.146.86.34:5984/_node/couchdb@115.146.86.34/_config/chttpd/bind_address" --data '"0.0.0.0"'



#the rest should 
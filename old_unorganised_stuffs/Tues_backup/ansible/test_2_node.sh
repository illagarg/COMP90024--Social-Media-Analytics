docker pull couchdb:2.1.1

export declare nodes=(115.146.86.96 115.146.86.172 115.146.86.34 115.146.86.170)
export masternode=`echo ${nodes} | cut -f1 -d' '`
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=admin

docker create couchdb:2.1.1 -–ip=${node}; done

declare conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d '\n'`)

for node in ${nodes[@]}}; do docker create couchdb:2.1.1 -–ip=${node}; done

declare conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d '\n'`)

for cont in "${conts[@]}"; do docker start ${cont}; done
sleep 3


for (( i=0; i<${size}; i++ )); do
    docker exec ${conts[${i}]} \
      bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
    docker exec ${conts[${i}]} \
      bash -c "echo \"-name couchdb@${nodes[${i}]}\" >> /opt/couchdb/etc/vm.args"
done

for cont in "${conts[@]}"; do docker restart ${cont}; done
sleep 3

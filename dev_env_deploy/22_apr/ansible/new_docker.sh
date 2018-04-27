docker pull couchdb:2.1.1

export declare nodes=(115.146.86.96 115.146.86.172 115.146.86.34 115.146.86.170)
export masternode=`echo ${nodes} | cut -f1 -d' '`
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=admin

#what does -d couchdb do?
for node in ${nodes[@]}}; do docker run -e COUCHDB_USER=${user} -e COUCHDB_PASSWORD=${pass} -p 5984:5984 -d couchdb; done
sleep 3

#Set the CouchDB cluster (deleting the default nonode@nohost node from the configuration)
for node in "${nodes[@]}"; do     
    curl -XPUT "http://${node}:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""    
    curl -XPUT "http://${user}:${pass}@${node}:5984/_node/couchdb@${node}/_config/chttpd/bind_address" --data '"0.0.0.0"'
done
for node in "${nodes[@]}"; do     
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json" \
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\", \
        \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\", \
        \"remote_node\": \"${node}\", \
        \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"
done
for node in "${nodes[@]}"; do     
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json" \
      --data "{\"action\": \"add_node\", \"host\":\"${node}\", \
        \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
done
curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}" 
rev=`curl -XGET "http://172.17.0.2:5986/_nodes/nonode@nohost" --user "${user}:${pass}" | sed -e 's/[{}"]//g' | cut -f3 -d:`
curl -X DELETE "http://172.17.0.2:5986/_nodes/nonode@nohost?rev=${rev}"  --user "${user}:${pass}"
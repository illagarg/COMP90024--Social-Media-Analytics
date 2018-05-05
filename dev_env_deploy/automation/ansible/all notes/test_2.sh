declare nodes=(115.146.86.34 115.146.86.96 115.146.86.172)
export masternode=`echo ${nodes} | cut -f1 -d' '` #the first element in that array
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=password



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
rev=`curl -XGET "http://115.146.86.96:5986/_nodes/nonode@nohost" --user "${user}:${pass}" | sed -e 's/[{}"]//g' | cut -f3 -d:`
curl -X DELETE "http://115.146.86.34:5986/_nodes/nonode@nohost?rev=${rev}"  --user "${user}:${pass}"



cluster setup: enabling cluster done?
{"ok":true}
{"ok":true}
{"ok":true}
YES
cluster set up: add node done?
{"error":"conflict","reason":"Document update conflict."}
{"ok":true}
{"error":"bad_request","reason":"Add node failed. Invalid Host and/or Port."}
YES
finishing setup done?
{"ok":true}
YES master node process has done
deleting nonode@nohost
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:17 --:--:--     0curl: (7) Failed to connect to 172.17.0.2 port 5986: No route to host
curl: (7) Failed to connect to 172.17.0.2 port 5986: No route to host

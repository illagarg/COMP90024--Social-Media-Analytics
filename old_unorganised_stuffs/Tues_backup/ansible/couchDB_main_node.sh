docker pull couchdb:2.1.1

export declare -a nodes=(115.146.86.96 115.146.86.172 115.146.86.34)
export masternode=`echo ${nodes} | cut -f1 -d' '`
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=password


for node in ${nodes[@]}}; do docker create -d  -v ~/data:/opt/couchdb/data -p 5984:5984 -–ip=${node} apache/couchdb:2.1.1; done

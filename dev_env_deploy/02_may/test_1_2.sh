#mkdir /extra/etc/local.d/1.ini
#docker create --net=host --volume /extra/data:/opt/couchdb/data --volume /extra/etc/local.d:/opt/couchdb/etc/local.d  couchdb:2.1.1



echo "Cleaning up the ~data folder"
rm ~/data
mkdir ~/data/data
mkdir ~/data/etc/local.d
rm ~/data/etc/local.d/*
echo ""
echo "Creating ini file "
touch ~/data/etc/local.d/1.ini
echo ""
echo "Declaring nodes, master nodes variables"
declare nodes=(115.146.86.96 115.146.86.34 115.146.86.172)
export masternode=`echo ${nodes} | cut -f1 -d' '` #the first element in that array
export othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user=admin
export pass=password
echo ""

echo "Creating docker container"
docker create --net=host -p 5984:5984 --volume ~/data/data:/opt/couchdb/data --volume ~/data/etc/local.d:/opt/couchdb/etc/local.d  apache/couchdb:2.1.1
echo ""
echo "DOES DECLARE CONTS WORK?"
declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d"\n"`)

echo "YES"
echo ""
for cont in "${conts[@]}"; do docker start ${cont}; done

sleep 3

echo "write things to the config files"
docker exec ${conts[0]} \
bash -c "echo \"-setcookie couchdb_cluster\" >> /opt/couchdb/etc/vm.args"
docker exec ${conts[0]} \
bash -c "echo \"-name couchdb@115.146.86.96\" >> /opt/couchdb/etc/vm.args"
echo ""
echo "restart container after"
for cont in "${conts[@]}"; do docker restart ${cont}; done
sleep 3
echo ""
echo "SETTING UP ADMIN AND ADDING NODES"

curl -XPUT "http://localhost:5984/_node/_local/_config/admins/${user}" --data "\"${pass}\""

curl -XPUT "http://${user}:${pass}@localhost:5984/_node/couchdb@115.146.86.96/_config/chttpd/bind_address" --data '"0.0.0.0"'

curl 115.146.86.96:5984

echo "yes"

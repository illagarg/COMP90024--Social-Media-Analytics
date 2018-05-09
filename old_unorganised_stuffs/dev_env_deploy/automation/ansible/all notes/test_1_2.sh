



mkdir /extra/data
mkdir /extra/etc
mkdir /extra/etc/local.d
rm /extra/etc/local.d/*
touch /extra/etc/local.d/1.ini
docker create --net=host --volume /extra/data:/opt/couchdb/data --volume /extra/etc/local.d:/opt/couchdb/etc/local.d  couchdb:2.1.1


rm ~/data
mkdir ~/data/etc/local.d
rm ~/data/etc/local.d/*
touch ~/data/etc/local.d/1.ini


import couchdb
import json
from cloudant import CouchDB

server = couchdb.Server( url='http://115.146.86.96:5984')#Top visited cities in Australia

admin = "admin"
password = "password"
server1 = "http://admin:password@115.146.86.96:5984"

try:
    couch = couchdb.Server(server1)
except:
    print("Cannot find CouchDB Server ... Exiting\n")
db=server['tourism_aurin']
d5 = 'tourism' 
if d5 in server:
 	dbn5= couch[d5]
else:
 	dbn5 = couch.create[d5]
touristlist={}
with open("sc1.json", "r", encoding="utf8") as sc1:
        map1 = json.load(sc1)
        for row in map1["features"]:
             city=row['cityname']
             for docid in db.view('City/'+city):
                 if docid['key']:
                     i = docid['key']
                     touristlist[city]=i
dict_tour={key: 0 for key in touristlist}
db1=server['twitter']
for docid in db1.view('Names/Texts'):
	for city in touristlist:
		for word in touristlist[city]:
			if word in docid['value']:
				dict_tour[city]+=1
dt = json.dumps(dict_tour)
tour_doc = {'results':dt}
for id in dbn5:
	if id.startswith("_"):
		pass
	else:
		dbn5.delete(dbn5[id])
dbn5.save(tour_doc)
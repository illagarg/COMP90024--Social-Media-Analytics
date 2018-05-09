import couchdb
from cloudant import CouchDB
import json

cdit = {} #dictionary to store the names of the cities and the number of posts in each city
dit = {} #dictionary to store the names and the sum of sentimental score of each city
resultdit = {}
server = couchdb.Server( url='http://115.146.86.96:5984') #connecting to the server

#DB server connection
db = server['twitter']

# collecting the data from the views.
# map reduce is used in the database server itself
for item in db.view('Names/Cities'):
	if item.value<0: #used to check for the negative numbers as the isnumeric() function does not allow the negative numbers
		c1 = abs(item.value)
		c = str(c1)
		d = unicode(c, 'utf-8')
		if d.isnumeric():
			if item.key in dit.keys():
				dit[item.key] = dit[item.key] - c1
				cdit[item.key] = cdit[item.key] + 1
			else:
				dit[item.key] = 0 - c1
				cdit[item.key] = 1
	else:
		c = str(item.value)
		d = unicode(c, 'utf-8')
		if d.isnumeric():
			if item.key in dit.keys():
				dit[item.key] = dit[item.key] + int(item.value)
				cdit[item.key] = cdit[item.key] + 1
			else:
				dit[item.key] = 0
				dit[item.key] = int(item.value)
				cdit[item.key] = 1

for item1 in dit:
	resultdit[item1] = float(dit[item1])/float(cdit[item1])







#storing the sum of the sentimental analysis score to the database in Json format
r = json.dumps(dit)
database_name = 'sentiment_sum'
admin = "admin"
password = "password"
server1 = "http://admin:password@115.146.86.96:5984"
document = {"results": r}
try:
    couch = couchdb.Server(server1)
    if database_name in server:
    	database = couch[database_name]
    else:
    	database = couch.create(database_name)
    print("DataBase Intialized")
    print database
except:
    print("Cannot find CouchDB Server ... Exiting\n")
for id in database:
	if id.startswith("_"):
		pass
	else:
		database.delete(database[id])
database.save(document)



#Storing the number of posts per city in the database in Json format
r1 = json.dumps(cdit)
doc1 = {"count": r1}
dbname = 'posts_per_city'
if dbname in couch:
	dbn = couch[dbname]
else:
	dbn = couch.create(dbname)
for id in dbn:
	if id.startswith("_"):
		pass
	else:
		dbn.delete(dbn[id])

dbn.save(doc1)

#Storing the ratio of the sentimental analysis to the number of posts to the database in Json format
resultset = json.dumps(resultdit)
resdoc = {'results' : resultset}
d2 = 'sentiment_ratio'
if d2 in couch:
	dbn1 = couch[d2]
else:
	dbn1 = couch.create(d2)
for id in dbn1:
	if id.startswith("_"):
		pass
	else:
		dbn1.delete(dbn1[id])
dbn1.save(resdoc)

userdict = {}

for docid in db.view('User/user'):
	if docid['key'] in userdict.keys():
		if docid['value'] in userdict.get(docid['key']):
			pass
		else:
			userdict[docid['key']].append(docid['value']) 
	else:
		userdict[docid['key']]=[docid['value']]
ud = json.dumps(userdict)
d1 = 'dist_user'
doc2 = {'distcount': ud}
if d1 in couch:
	dbn2 = couch[d1]
else:
	dbn2 = couch.create(d1)
for id in dbn2:
	if id.startswith("_"):
		pass
	else:
		dbn2.delete(dbn2[id])
dbn2.save(doc2)


print userdict
print r
print cdit


#Number of tweets related to the crime
crime = {}
m = open('crime.txt','r')
print("READ FILE")
for line in m:
	for item in db.view('Names/Texts'):
		if line in item.value:
			if item.key in crime.keys():
				crime[item.key] = crime[item.key] + 1
			else:
				crime[item.key] = 1
Crime = json.dumps(crime)
doc3 = {'Crime_Count':Crime}
d3 = 'crime'
if d3 in couch:
	dbn3 = couch[d3]
else:
	dbn3 = couch.create(d3)
for id in dbn3:
	if id.startswith("_"):
		pass
	else:
		dbn3.delete(dbn3[id])
dbn3.save(doc3)
print crime


langcitydit = {'Adelaide':{},'Alice Springs':{},'Brisbane':{},'Canberra':{},'Hobart':{},'Mackay':{},'Melbourne':{},'Perth':{},'Sydney':{},'Wollongong':{},'Gold Coast':{}, 'Newcastle':{}}
for item in db.view('Names/Language'):
	for line in langcitydit:
		if line in item.key:
			if item.value in langcitydit[line].keys():
				langcitydit[line][item.value] = langcitydit[line][item.value] + 1
			else:
				langcitydit[line][item.value] = 1

d4 = "language"
if d4 in server:
    db = couch[d4]
else:
    db = couch.create(d4)
resultset = json.dumps(langcitydit)
resdoc = {'results' : resultset}
dbn4 = server[d4]
for id in dbn4:
	if id.startswith("_"):
		pass
	else:
		dbn4.delete(dbn4[id])
dbn4.save(resdoc)
print langcitydit
print "complete"
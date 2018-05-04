import couchdb
from cloudant import CouchDB
count = 0
cdit = {} #dictionary to store the names of the cities and the number of posts in each city
dit = {} #dictionary to store the names and the sum of sentimental score of each city
server = couchdb.Server( url='http://115.146.86.170:5984') #connecting to the server

#DB server connection
db = server['twitter']

# collecting the data from the views.
# map reduce is used in the database server itself
for item in db.view('Names/Cities'):
	count = count +1
	print item.value
	if item.value<0: #used to check for the negative numbers as the isnumeric() function does not allow the negative numbers
		c1 = abs(item.value)
		c = str(c1)
		d = unicode(c, 'utf-8')
		if d.isnumeric():
			if item.key in dit.keys():
				print c1
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
				print item.value
				dit[item.key] = dit[item.key] + int(item.value)
				cdit[item.key] = cdit[item.key] + 1
			else:
				dit[item.key] = 0
				dit[item.key] = int(item.value)
				cdit[item.key] = 1
				

print dit
print cdit
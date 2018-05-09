import couchdb
from couchdb.design import ViewDefinition

admin = 'admin'
password = 'password'
server = couchdb.Server( 'http://admin:password@115.146.86.96:5984') #connecting to the server

#DB server connection
db = server['twitter']

#view creation
view1 = ViewDefinition('Names', 'Cities', 'function(doc) {emit(doc.tweet_data.place.name, doc.sentiment);}')
view1.get_doc(db)
view1.sync(db)

view2 = ViewDefinition('Names', 'Language', 'function(doc) {emit(doc.tweet_data.place.name, doc.tweet_data.user.lang);}')
view2.get_doc(db)	
view2.sync(db)

view3 = ViewDefinition('Names', 'Texts', 'function(doc) {emit(doc.tweet_data.place.name, doc.tweet_data.text);}')
view3.get_doc(db)
view3.sync(db)

view4 = ViewDefinition('User', 'user', 'function(doc) {emit(doc.tweet_data.place.name, doc.tweet_data.user.screen_name);}')
view4.get_doc(db)
view4.sync(db)

print "View Creation completed"
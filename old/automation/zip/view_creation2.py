import couchdb
from couchdb.design import ViewDefinition

admin = 'admin'
password = 'password'
server = couchdb.Server( 'http://admin:password@115.146.86.96:5984')

db = server['sentiment_ratio']

view1 = ViewDefinition('Res', 'res', 'function(doc) {emit(doc.results, 1);}')
view1.get_doc(db)
view1.sync(db)

db1 = server['sentiment_sum']

view2 = ViewDefinition('Res', 'res', 'function(doc) {emit(doc.results, 1);}')
view2.get_doc(db1)
view2.sync(db1)

db2 = server['posts_per_city']

view2 = ViewDefinition('Res', 'res', 'function(doc) {emit(doc.count, 1);}')
view2.get_doc(db2)
view2.sync(db2)

db3 = server['dist_user']

view3 = ViewDefinition('Res', 'res', 'function(doc) {emit(doc.distcount, 1);}')
view3.get_doc(db3)
view3.sync(db3)

db4 = server['language']

view4 = ViewDefinition('Res', 'res', 'function(doc) {emit(doc.results, 1);}')
view4.get_doc(db4)
view4.sync(db4)

print "view creation2 completed"
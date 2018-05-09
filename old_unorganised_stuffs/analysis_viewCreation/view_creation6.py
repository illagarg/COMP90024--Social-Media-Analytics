import couchdb
from couchdb.design import ViewDefinition

admin = 'admin'
password = 'password'
server = couchdb.Server( 'http://admin:password@115.146.86.96:5984') #connecting to the server

#DB server connection
db = server['tourism_aurin']

#view creation
view1 = ViewDefinition('City', 'Adelaide', 'function(doc) {emit(doc.Adelaide, 1);}')
view1.get_doc(db)
view1.sync(db)

view2 = ViewDefinition('City', 'Brisbane', 'function(doc) {emit(doc.Brisbane, 1);}')
view2.get_doc(db)
view2.sync(db)

view3 = ViewDefinition('City', 'Canberra', 'function(doc) {emit(doc.Canberra, 1);}')
view3.get_doc(db)
view3.sync(db)

view4 = ViewDefinition('City', 'Melbourne', 'function(doc) {emit(doc.Melbourne, 1);}')
view4.get_doc(db)
view4.sync(db)

view5 = ViewDefinition('City', 'Perth', 'function(doc) {emit(doc.Perth, 1);}')
view5.get_doc(db)
view5.sync(db)

view6 = ViewDefinition('City', 'Sydney', 'function(doc) {emit(doc.Sydney, 1);}')
view6.get_doc(db)
view6.sync(db)

view7 = ViewDefinition('City', 'Wollongong', 'function(doc) {emit(doc.Wollongong, 1);}')
view7.get_doc(db)
view7.sync(db)

view8 = ViewDefinition('City', 'Mackay', 'function(doc) {emit(doc.Mackay, 1);}')
view8.get_doc(db)
view8.sync(db)

view9 = ViewDefinition('City', 'Hobart', 'function(doc) {emit(doc.Hobart, 1);}')
view9.get_doc(db)
view9.sync(db)

view10 = ViewDefinition('City', 'Gold Coast', 'function(doc) {emit(doc.(Gold Coast), 1);}')
view10.get_doc(db)
view10.sync(db)

view11 = ViewDefinition('City', 'Newcastle', 'function(doc) {emit(doc.Newcastle, 1);}')
view11.get_doc(db)
view11.sync(db)

view12 = ViewDefinition('City', 'Alice Springs', 'function(doc) {emit(doc.Alice Springs, 1);}')
view12.get_doc(db)
view12.sync(db)


print "View Creation completed for tourism_aurin"
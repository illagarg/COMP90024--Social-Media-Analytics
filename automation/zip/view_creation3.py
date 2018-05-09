import couchdb
from couchdb.design import ViewDefinition

admin = 'admin'
password = 'password'
server = couchdb.Server( 'http://admin:password@115.146.86.96:5984') #connecting to the server

#DB server connection
db = server['income']

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

print "View Creation completed for income"

db1 = server['population']

#view creation
view21 = ViewDefinition('City', 'Adelaide', 'function(doc) {emit(doc.Adelaide, 1);}')
view21.get_doc(db1)
view21.sync(db1)

view22 = ViewDefinition('City', 'Brisbane', 'function(doc) {emit(doc.Brisbane, 1);}')
view22.get_doc(db1)
view22.sync(db1)

view23 = ViewDefinition('City', 'Canberra', 'function(doc) {emit(doc.Canberra, 1);}')
view23.get_doc(db1)
view23.sync(db1)

view24 = ViewDefinition('City', 'Melbourne', 'function(doc) {emit(doc.Melbourne, 1);}')
view24.get_doc(db1)
view24.sync(db1)

view25 = ViewDefinition('City', 'Perth', 'function(doc) {emit(doc.Perth, 1);}')
view25.get_doc(db1)
view25.sync(db1)

view26 = ViewDefinition('City', 'Sydney', 'function(doc) {emit(doc.Sydney, 1);}')
view26.get_doc(db1)
view26.sync(db1)

view27 = ViewDefinition('City', 'Wollongong', 'function(doc) {emit(doc.Wollongong, 1);}')
view27.get_doc(db1)
view27.sync(db1)

view28 = ViewDefinition('City', 'Mackay', 'function(doc) {emit(doc.Mackay, 1);}')
view28.get_doc(db1)
view28.sync(db1)

view29 = ViewDefinition('City', 'Hobart', 'function(doc) {emit(doc.Hobart, 1);}')
view29.get_doc(db1)
view29.sync(db1)

view210 = ViewDefinition('City', 'Gold Coast', 'function(doc) {emit(doc.Gold Coast, 1);}')
view210.get_doc(db1)
view210.sync(db1)

view211 = ViewDefinition('City', 'Newcastle', 'function(doc) {emit(doc.Newcastle, 1);}')
view211.get_doc(db1)
view211.sync(db1)

view212 = ViewDefinition('City', 'Alice Springs', 'function(doc) {emit(doc.Alice Springs, 1);}')
view212.get_doc(db1)
view212.sync(db1)

print "View Creation completed for population"


db2 = server['lang_aurin']

#view creation
view31 = ViewDefinition('Result', 'Adelaide', 'function(doc) {emit(doc.Adelaide, 1);}')
view31.get_doc(db2)
view31.sync(db2)

view32 = ViewDefinition('Result', 'Brisbane', 'function(doc) {emit(doc.Brisbane, 1);}')
view32.get_doc(db2)
view32.sync(db2)

view33 = ViewDefinition('Result', 'Canberra', 'function(doc) {emit(doc.Canberra, 1);}')
view33.get_doc(db2)
view33.sync(db2)

view34 = ViewDefinition('Result', 'Melbourne', 'function(doc) {emit(doc.Melbourne, 1);}')
view34.get_doc(db2)
view34.sync(db2)

view35 = ViewDefinition('Result', 'Perth', 'function(doc) {emit(doc.Perth, 1);}')
view35.get_doc(db2)
view35.sync(db2)

view36 = ViewDefinition('Result', 'Sydney', 'function(doc) {emit(doc.Sydney, 1);}')
view36.get_doc(db2)
view36.sync(db2)

view37 = ViewDefinition('Result', 'Wollongong', 'function(doc) {emit(doc.Wollongong, 1);}')
view37.get_doc(db2)
view37.sync(db2)

view38 = ViewDefinition('Result', 'Mackay', 'function(doc) {emit(doc.Mackay, 1);}')
view38.get_doc(db2)
view38.sync(db2)

view39 = ViewDefinition('Result', 'Hobart', 'function(doc) {emit(doc.Hobart, 1);}')
view39.get_doc(db2)
view39.sync(db2)

view310 = ViewDefinition('Result', 'Gold Coast', 'function(doc) {emit(doc.(Gold Coast), 1);}')
view310.get_doc(db2)
view310.sync(db2)

view311 = ViewDefinition('Result', 'Newcastle', 'function(doc) {emit(doc.Newcastle, 1);}')
view311.get_doc(db2)
view311.sync(db2)

view312 = ViewDefinition('Result', 'Alice Springs', 'function(doc) {emit(doc.Alice Springs, 1);}')
view312.get_doc(db2)
view312.sync(db2)

print "View Creation completed lang_aurin"

db4 = server['tourism_aurin']

#view creation
view41 = ViewDefinition('City', 'Adelaide', 'function(doc) {emit(doc.Adelaide, 1);}')
view41.get_doc(db4)
view41.sync(db4)

view42 = ViewDefinition('City', 'Brisbane', 'function(doc) {emit(doc.Brisbane, 1);}')
view42.get_doc(db4)
view42.sync(db4)

view43 = ViewDefinition('City', 'Canberra', 'function(doc) {emit(doc.Canberra, 1);}')
view43.get_doc(db4)
view43.sync(db4)

view44 = ViewDefinition('City', 'Melbourne', 'function(doc) {emit(doc.Melbourne, 1);}')
view44.get_doc(db4)
view44.sync(db4)

view45 = ViewDefinition('City', 'Perth', 'function(doc) {emit(doc.Perth, 1);}')
view45.get_doc(db4)
view45.sync(db4)

view46 = ViewDefinition('City', 'Sydney', 'function(doc) {emit(doc.Sydney, 1);}')
view46.get_doc(db4)
view46.sync(db4)

view47 = ViewDefinition('City', 'Wollongong', 'function(doc) {emit(doc.Wollongong, 1);}')
view47.get_doc(db4)
view47.sync(db4)

view48 = ViewDefinition('City', 'Mackay', 'function(doc) {emit(doc.Mackay, 1);}')
view48.get_doc(db4)
view48.sync(db4)

view49 = ViewDefinition('City', 'Hobart', 'function(doc) {emit(doc.Hobart, 1);}')
view49.get_doc(db4)
view49.sync(db4)

view410 = ViewDefinition('City', 'Gold Coast', 'function(doc) {emit(doc.(Gold Coast), 1);}')
view410.get_doc(db4)
view410.sync(db4)

view411 = ViewDefinition('City', 'Newcastle', 'function(doc) {emit(doc.Newcastle, 1);}')
view411.get_doc(db4)
view411.sync(db4)

view412 = ViewDefinition('City', 'Alice Springs', 'function(doc) {emit(doc.Alice Springs, 1);}')
view412.get_doc(db4)
view412.sync(db4)


print "View Creation completed for tourism_aurin"



db5 = server['offences']

#view creation
view51 = ViewDefinition('CrimeRes', 'Adelaide', 'function(doc) {emit(doc.Adelaide, 1);}')
view51.get_doc(db5)
view51.sync(db5)

view52 = ViewDefinition('CrimeRes', 'Brisbane', 'function(doc) {emit(doc.Brisbane, 1);}')
view52.get_doc(db5)
view52.sync(db5)

view53 = ViewDefinition('CrimeRes', 'Canberra', 'function(doc) {emit(doc.Canberra, 1);}')
view53.get_doc(db5)
view53.sync(db)

view54 = ViewDefinition('CrimeRes', 'Melbourne', 'function(doc) {emit(doc.Melbourne, 1);}')
view54.get_doc(db5)
view54.sync(db5)

view55 = ViewDefinition('CrimeRes', 'Perth', 'function(doc) {emit(doc.Perth, 1);}')
view55.get_doc(db5)
view55.sync(db5)

view56 = ViewDefinition('CrimeRes', 'Sydney', 'function(doc) {emit(doc.Sydney, 1);}')
view56.get_doc(db5)
view56.sync(db5)

view57 = ViewDefinition('CrimeRes', 'Wollongong', 'function(doc) {emit(doc.Wollongong, 1);}')
view57.get_doc(db5)
view57.sync(db5)

view58 = ViewDefinition('CrimeRes', 'Mackay', 'function(doc) {emit(doc.Mackay, 1);}')
view58.get_doc(db5)
view58.sync(db5)

view59 = ViewDefinition('CrimeRes', 'Hobart', 'function(doc) {emit(doc.Hobart, 1);}')
view59.get_doc(db5)
view59.sync(db5)

view510 = ViewDefinition('CrimeRes', 'Gold Coast', 'function(doc) {emit(doc.(Gold Coast), 1);}')
view510.get_doc(db5)
view510.sync(db5)

view511 = ViewDefinition('CrimeRes', 'Newcastle', 'function(doc) {emit(doc.Newcastle, 1);}')
view511.get_doc(db5)
view511.sync(db5)

view512 = ViewDefinition('CrimeRes', 'Alice Springs', 'function(doc) {emit(doc.Alice Springs, 1);}')
view512.get_doc(db5)
view512.sync(db5)

print "View Creation completed for offences"
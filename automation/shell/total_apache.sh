#!/usr/bin/env bash

#install and run the harvester, analyser, and put aurin data onto the DB
sudo apt-get update &> /dev/null
sudo apt-get install -y vim &> /dev/null
sudo apt-get -y install python-pip &> /dev/null
#--quiet
sudo pip install couchdb --quiet
sudo pip install cloudant --quiet
sudo pip install tweepy --quiet
sudo pip install afinn --quiet
echo "installed pakages for Harvester and analyser"

echo "starting harvester and analyser deployment"
cd zip
#harvester can be deployed
sudo nohup python -u /home/ubuntu/zip/TwitterHarvester.py &> harvester.out&
#wait for 30 sec
sleep 30
#done VC1
sudo nohup python -u /home/ubuntu/zip/view_creation1.py &> view_creation1.out&
#file can be read
sudo nohup python -u /home/ubuntu/zip/analysis.py &> analysis.out&
#need to add this file
sudo nohup python3 -u /home/ubuntu/zip/analysis1.py &> analysis1.out&
#this is done too
sudo nohup python -u /home/ubuntu/zip/view_creation2.py &> view_creation2.out&

echo "updating aurin data to database"

(curl -d "@Population.json" -H "Content-Type: application/json" -X POST http://115.146.86.96:5984/population

curl -d "@Language.json" -H "Content-Type: application/json" -X POST http://115.146.86.96:5984/lang_aurin

curl -d "@SortedIncome.json" -H "Content-Type: application/json" -X POST http://115.146.86.96:5984/income

curl -d "@tourism_aurin.json" -H "Content-Type: application/json" -X POST http://115.146.86.96:5984/tourism_aurin

curl -d "@offence.json" -H "Content-Type: application/json" -X POST http://115.146.86.96:5984/offences) &> /dev/null 

sudo nohup python -u /home/ubuntu/zip/view_creation3.py &> view_creation3.out&


echo "deploying programs has done, now install web service"

sudo apt-get install -y apt-utils curl apache2 apache2-utils &> /dev/null

sudo apt-get -y install python3 libapache2-mod-wsgi-py3 &> /dev/null
#sudo ln /usr/bin/python3 /usr/bin/python
sudo apt-get -y install python3-pip &> /dev/null
#sudo ln /usr/bin/pip3 /usr/bin/pip

#--quiet
sudo pip3 install django --quiet
sudo pip3 install couchdb --quiet
echo "installed all the stuffs"



#replace the config files



#assuming all my config files are in the ~/ dir

#vi /etc/apache2/sites-available/000-default.conf

echo "hopefully the file has been upziped and in ~/zip"

sudo cp -f /home/ubuntu/zip/000-default.conf /etc/apache2/sites-available/000-default.conf
sudo cp -f /home/ubuntu/zip/apache2.conf /etc/apache2/apache2.conf
sudo mkdir /var/www/logs
sudo chmod 777 /var/www/logs

sudo cp -R /home/ubuntu/zip/cccteam17 /var/www/

sudo chmod -R 777 /var/www/cccteam17/

echo "try to start manage.py"
sudo nohup python3 /var/www/cccteam17/manage.py runserver &

sudo systemctl restart apache2.service



echo "done with apache restarting..."




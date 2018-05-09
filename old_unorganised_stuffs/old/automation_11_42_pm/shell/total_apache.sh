#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y apt-utils curl apache2 apache2-utils
sudo apt-get install -y vim
sudo apt-get -y install python3 libapache2-mod-wsgi-py3
#sudo ln /usr/bin/python3 /usr/bin/python
sudo apt-get -y install python3-pip
#sudo ln /usr/bin/pip3 /usr/bin/pip


#--quiet
sudo pip3 install django --quiet
echo "installed all the stuffs"



#replace the config files



#assuming all my config files are in the ~/ dir

#vi /etc/apache2/sites-available/000-default.conf

echo "hopefully the file has been upziped and in ~/zip"

sudo cp -f /home/ubuntu/zip/000-default.conf /etc/apache2/sites-available/000-default.conf
sudo cp -f /home/ubuntu/zip/apache2.conf /etc/apache2/apache2.conf
sudo mkdir /var/www/logs
sudo chmod 777 /var/www/logs

cp -R /home/ubuntu/zip/cccteam17 /var/www/


sudo chmod 777 /var/www/logs

cp -R /home/ubuntu/zip/cccteam17 /var/www/
echo "try to start manage.py"
sudo nohup python3 /var/www/cccteam17/manage.py runserver &

sudo systemctl restart apache2.service


#install and run the harvester, analyser, and put aurin data onto the DB

sudo apt-get -y install python-pip
#--quiet
sudo pip install couchdb --quiet
sudo pip install cloudant --quiet
sudo pip install tweepy --quiet
sudo pip install afinn --quiet

cd zip

sudo nohup python -u /home/ubuntu/zip/TwitterHarvester.py &> harvester.out&
#wait for 30 sec
sleep 30

sudo nohup python -u /home/ubuntu/zip/view_creation1.py &> view_creation1.out&

sudo nohup python -u /home/ubuntu/zip/analysis.py &> analysis.out&

sudo nohup python3 -u /home/ubuntu/zip/analysis1.py &> analysis1.out&

sudo nohup python -u /home/ubuntu/zip/view_creation2.py &> view_cr


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
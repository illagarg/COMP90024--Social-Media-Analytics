#replace the config files



#assuming all my config files are in the ~/ dir

#vi /etc/apache2/sites-available/000-default.conf



sudo cp -f 000-default.conf /etc/apache2/sites-available/000-default.conf
sudo cp -f apache2.conf /etc/apache2/apache2.conf
sudo mkdir /var/www/logs
sudo chmod 777 /var/www/logs

sudo nohup python /var/www/cccteam17/manage.py &

sudo systemctl restart apache2.service
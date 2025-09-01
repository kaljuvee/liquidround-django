#!/bin/bash
sudo aptitude update
debconf-set-selections <<< 'mysql-server mysql-server/root_password password pass'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password pass'
sudo aptitude -y install postgresql git-core python-dev python-setuptools python-pip libjpeg-dev zlib1g-dev libpng12-dev build-essential libpcre3 libpcre3-dev postgresql postgresql-contrib python-psycopg2


#sudo cp /vagrant/deploy/nginx.conf /etc/nginx/nginx.conf
#sudo cp /vagrant/deploy/nginx-site /etc/nginx/sites-available/nginx-site
#sudo ln -s /etc/nginx/sites-available/nginx-site /etc/nginx/sites-enabled/nginx-site
#sudo cp /vagrant/deploy/php.ini /etc/php5/apache2/php.ini
#

#mysql -u root -ppass -e "create database wheel"

#sudo a2enmod rewrite
#sudo service apache2 restart

#cd /tmp
#git clone https://github.com/django/django.git
#cd /tmp/django
#git checkout stable/1.7.x
#sudo python setup.py install

sudo pip install django==1.8.2
sudo pip install uwsgi
sudo pip install djangorestframework
sudo pip install markdown
sudo pip install django-filter

#sudo pip install django-bootstrap3
#sudo pip install Pillow
#sudo pip install django-resized
#sudo pip install django-imagekit
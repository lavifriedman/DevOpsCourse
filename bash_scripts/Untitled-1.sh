#!/bin/bash
sudo apt update
sudo apt -y install apache2 php
sudo mkdir /var/www/lavi_domain
sudo chown -R $USER:$USER /var/www/lavi_domain
sudo echo '<VirtualHost *:80>' > /etc/apache2/sites-available/lavi_domain.conf
sudo echo '    ServerName lavi_domain' >> /etc/apache2/sites-available/lavi_domain.conf
sudo echo '    ServerAlias www.lavi_domain' >> /etc/apache2/sites-available/lavi_domain.conf
sudo echo '    ServerAdmin webmaster@localhost' >> /etc/apache2/sites-available/lavi_domain.conf
sudo echo '    DocumentRoot /var/www/lavi_domain' >> /etc/apache2/sites-available/lavi_domain.conf
sudo echo '    ErrorLog ${APACHE_LOG_DIR}/error.log' >> /etc/apache2/sites-available/lavi_domain.conf
sudo echo '    CustomLog ${APACHE_LOG_DIR}/access.log combined' >> /etc/apache2/sites-available/lavi_domain.conf
sudo echo '</VirtualHost>' >> /etc/apache2/sites-available/lavi_domain.conf
sudo a2ensite lavi_domain
sudo a2dissite 000-default
sudo systemctl restart apache2

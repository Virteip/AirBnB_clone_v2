#!/usr/bin/env bash
#Sets up your web servers for the deployment.
sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Holberton" > /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0

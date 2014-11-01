#!/bin/bash

# Update
sudo apt-get update
sudo apt-get upgrade -y

# Install Java Runtime
sudo apt-get install -y openjdk-6-jre

# Install ElasticSearch
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.deb
dpkg -i elasticsearch-1.3.4.deb

# Configure ElasticSearch
sudo sed -i "s/#network.bind_host: .*/network.bind_host: localhost/" /etc/elasticsearch/elasticsearch.yml
sudo service elasticsearch restart
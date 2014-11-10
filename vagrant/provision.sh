#!/bin/bash

# Update
sudo apt-get update
sudo apt-get upgrade -y

# Install pip
sudo apt-get install -y python3-pip

# Install pip packages
sudo pip3 install -U numpy
sudo pip3 install -U scipy
sudo pip3 install -U scikit-learn
sudo pip3 install -U nltk
sudo pip3 install -U elasticsearch

# Download nltk packages
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader wordnet
python3 -m nltk.downloader punkt

# Install Java Runtime
sudo apt-get install openjdk-7-jre-headless -y

# Add Sources
sudo wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo apt-key add -
echo 'deb http://packages.elasticsearch.org/elasticsearch/1.3/debian stable main' | sudo tee -a /etc/apt/sources.list

# Install ElasticSearch
sudo apt-get update
sudo apt-get install elasticsearch
sudo update-rc.d elasticsearch defaults 95 10
sudo /etc/init.d/elasticsearch start
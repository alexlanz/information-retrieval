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

# Download nltk packages
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader wordnet
python3 -m nltk.downloader punkt
#!/bin/bash

# Update
sudo apt-get update
sudo apt-get upgrade -y

# Install pip
sudo apt-get install -y python-pip python3-pip

# Install python module requirements
sudo apt-get install -y python3-numpy python3-scipy python3-matplotlib

# Install pip packages
sudo pip3 install -U numpy
sudo pip3 install -U scipy
sudo pip3 install -U scikit-learn
sudo pip3 install -U nltk
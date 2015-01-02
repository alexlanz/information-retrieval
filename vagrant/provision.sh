#!/bin/bash

# Update
apt-get update
apt-get upgrade -y

# Install pip
apt-get install -y python-pip python3-pip

# Install scikit
sudo apt-get install -y python-numpy python3-numpy python-scipy python3-scipy
sudo pip install -U scikit-learn
sudo pip3 install -U scikit-learn
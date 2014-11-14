#!/bin/bash

# Update
sudo apt-get update
sudo apt-get upgrade -y

# Install pip
sudo apt-get install -y python-pip

# Install Snap.py
wget http://snap.stanford.edu/snappy/release/snap-1.1-2.3-centos6.5-x64-py2.6.tar.gz
tar zxvf snap-1.1-2.3-centos6.5-x64-py2.6.tar.gz
cd snap-1.1-2.3-centos6.5-x64-py2.6/
sudo python setup.py install
cd ..
sudo rm -rf snap-1.1-2.3-centos6.5-x64-py2.6
sudo rm -rf snap-1.1-2.3-centos6.5-x64-py2.6.tar.gz
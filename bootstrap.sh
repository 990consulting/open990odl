#!/bin/sh
echo "***Installing git"
sudo yum -y install git
echo "***Installing Python dependencies"
sudo pip-3.4 install typing
echo "***Cloning open990"
git clone https://github.com/borenstein/open990
echo "***Bootstrap complete"

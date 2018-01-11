#!/bin/sh
echo "***Installing git"
sudo yum -y install git
echo "***Installing Python dependencies"
sudo pip-3.4 install typing
echo "***Bootstrap complete"

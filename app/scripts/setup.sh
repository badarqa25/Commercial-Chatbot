#!/bin/bash

# Update packages
sudo yum update -y

# Install Python 3 and pip
sudo yum install -y python3 python3-pip

# Install Nginx (new method for Amazon Linux 2023)
sudo yum install -y nginx

# Install Git
sudo yum install -y git

# Start and enable Nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Install virtualenv as regular user (not root)
pip3 install --user virtualenv

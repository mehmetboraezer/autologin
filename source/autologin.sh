#!/bin/bash

username=$1
passwd=$2

if [[ $username != `whoami` ]]
then
  echo "Invalid username provided"
  exit 1
fi

sudo /usr/bin/defaults write /Library/Preferences/com.apple.loginwindow.plist "autoLoginUser" $username

echo "$passwd" | sudo ./keygen.py 

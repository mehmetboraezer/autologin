#!/bin/bash

username=$1
password=$2

if ! id "$username" >/dev/null 2>&1; then
	echo "User does not exist"
fi

/usr/bin/defaults write /Library/Preferences/com.apple.loginwindow.plist "autoLoginUser" $username

echo "$password" | ./keygen.py 

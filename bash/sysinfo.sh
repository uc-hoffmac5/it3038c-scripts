#!/bin/bash
#this script will email us our us our user, IP, and hostname
emailaddress="hoffmac5@mail.uc.edu"
today=$(date +"%m-%d-%Y")
ip=$(/usr/sbin/ifconfig | grep ' inet 192' | awk '{print $2}')

printf -v content "User:\t%s\n My Hostname:\t%s\n My IP:\t%s\n" $USER $HOSTNAME $ip
mail -s "IT3038C Linux IP" $emailaddress <<< $content

#!/bin/bash
#this will email 4 facts about the machine
emailaddress=hoffmac5@mail.uc.edu
currentTime=$(date +"%m-%d-%Y--%H:%M:%S")
ipaddress=$(/usr/sbin/ifconfig | grep ' inet 192.168.33' | awk '{print $2}')

printf -v content "Machine Name:\t $HOSTNAME \n Bash Version:\t%s\n Current Date and Time\t%s \nIP Address:\t$ipaddress \n"  $BASH_VERSION $currentTime 

mail -s "IT3038 Lab 2" $emailaddress  <<<$content



#!/bin/bash

echo "---System Health Report---"

mkdir -p logs
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
logfile="logs/system_report_$timestamp.txt"

{

hostname #Host name
whoami #User
date #Current Date
uname -r #Linux Kernal Version
uptime #CPU Load
df -h #Disk Usage
free -h #Memory 
systemctl is-active apache2 #Check apache2 running
systemctl is-active ssh #Check ssh running

} | tee "$logfile"

echo "Report saved to: $logfile"


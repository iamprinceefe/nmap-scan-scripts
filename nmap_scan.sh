#!/bin/bash

# Check if the input file with IP addresses is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <ip_list_file>"
	exit 1
fi

# Read IP addresses from the provided file
ip_list_file=$1

# Check if the file exists
if [ ! -f "$ip_list_file" ]; then 
	echo "File not found: $ip_list_file"
	exit 1
fi

# Loop through each IP address in the file
while IFS= read -r ip; do
	echo "Scanning IP: $ip"
	#Run the Nmap scan
	nmap -sV "$ip" -oN "${ip}_scan.txt"
done < "$ip_list_file"

echo "All scans are complete." 

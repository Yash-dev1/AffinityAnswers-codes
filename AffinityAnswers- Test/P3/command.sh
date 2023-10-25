#!/bin/bash

URL="https://www.amfiindia.com/spages/NAVAll.txt" #provided URL

new="problem3.tsv"

curl -s "$URL" | awk -F';' 'NR>2 { print $4 "\t" $5 }' > "$new" # main command to downlod the data form URL

# curl is used to download the data from URL
# awk -F is used for splitting the fields seperated by ;  
# NR>2 applies the script only to the lines who have greater thatn 2 fields i.e. it kips the first two header lines in the file 


echo "data sent to $new"


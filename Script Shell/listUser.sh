#!/bin/bash
while read ligne
do
identifiant=$(echo "$ligne" | awk -F: '{ print $3 }')
if [ "$identifiant" -gt 100 ]
then
echo "$ligne"
fi
done < /etc/passwd

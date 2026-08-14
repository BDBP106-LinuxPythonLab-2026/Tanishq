#!/bin/bash

echo "Enter the file name;"
read file

if [ -e"$file" ];then
	echo "The file exits."
	exit 200
	
else 
    echo "The file does not exits."
    exit 201
fi    

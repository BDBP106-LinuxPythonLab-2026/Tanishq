#!/bin/bash
file=$1
echo "Enter the filename:$1"
read file

if [ -e "$file" ];then
	echo "The file exits"

       if [ -x "$file" ];then
	    echo "The file is executable"
       
       else 
	    echo "The file is not executable"
fi  
else
     echo "The file does not exit"
fi     
	




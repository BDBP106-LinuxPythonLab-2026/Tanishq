#!/bin/bash
age=$1
echo "Enter your age: $1"
read age

if [ "$age" -ge 18 ]
then	
    echo "You are an adult"
else
    echo "You are an minor"
fi    

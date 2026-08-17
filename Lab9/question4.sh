#!/bin/bash

echo $0
name=$1
age=$2

echo 'the first argument is: ',$1
echo 'the second argument is: ',$2

echo " the number of arguments passed to the script: ",$#
echo "the arguments passed to the script: ",$@

echo "the name of the script itself: ",$0

#!/bin/bash
maximum(){
	local a=$1
	local b=$2
	if [ $a -ge $b ];then
		echo $a
	else 
		echo $b
	fi
}
maximum_value=$( maximum 99 52 )
echo "maximum value is $maximum_value"


	



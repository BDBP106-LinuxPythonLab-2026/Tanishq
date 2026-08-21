#!/bin/bash

function divide {
           local a=$1
           local b=$2


	   if [ $b -ne 0 ];then
		   echo "Divisible by zero is not allowed"
	   
	   
	   local quotient=$(echo "scale=2;$a/$b" | bc)
	   local remainder=$(echo "$a%$b" | bc)
	   
	   echo "Quotient:$quotient"
	   echo "Remainder:$remainder"
	   
	   fi
   }	   
result=$(divide $1 $2)
echo "result is $result"

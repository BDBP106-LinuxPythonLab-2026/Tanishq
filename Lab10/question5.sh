#!/bin/bash
echo "Enter the score (0-100)"
read score

if [ $score -gt 90 ]&&[ $score -lt 100 ];then
	echo "Grade A."

elif [ $score -gt 80 ]&&[ $score -lt 89 ];then
	echo "Grade B."

elif [ $score -gt 70 ] &&[ $score -lt 79 ];then
	echo "Grade C."
	
elif [ $score -lt 70 ]&&[ $score -gt 0 ];then
         echo "fail."
fi	

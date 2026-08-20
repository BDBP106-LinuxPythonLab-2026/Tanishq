#!/bin/bash

if [ -e "BrainCancer.csv" ]; then
	echo "The file is exist"

else
	echo "The file is not exist"
fi	



#!/bin/bash

if [ -s "BrainCancer.csv" ]; then
	echo "The file is not empty"
else
	echo "The file is empty"
fi	


#!/bin/bash

if [ -f "BrainCancer.csv" ];then
	echo "The file is regular files"
else
	echo "The file is not regular"
fi	

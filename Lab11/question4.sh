#!/bin/bash
val1=Jayashree
val2=Nagesh
if [ $val1 > $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi
#here > is correctly interpreted as a string comparison operator
#since J comes N alphabetically

#!/bin/bash
val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi
#To use > as a comparision operator,it is escaped using \.
#Therefore,[ $val1 \>$val2 ] performs the intended string comparision without creating the unwanted file


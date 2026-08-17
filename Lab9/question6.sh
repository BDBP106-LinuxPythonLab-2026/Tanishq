#!/bin/bash
echo "$HOME"

bc_output=$(bc << EOF
scale=4
23934/44343
EOF
)
echo "the output for 23934/44343 is :" $bc_output

echo "the starting with the D in the home are :" "$HOME"/D*
 
echo "the lines contaning the username are " 
grep "$USER" /etc/passwd

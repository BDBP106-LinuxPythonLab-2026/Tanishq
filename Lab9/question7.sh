#!/bin/bash
mass=1
speed=3*10^8
energy=$(bc << EOF
$mass*$speed*$speed
EOF
)
echo "the energy mass equivalance is " $energy


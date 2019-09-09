#!/bin/bash
# Assuming that GGA and HSE job types are run on 128, 256, adn 320 ranks.
# Assuming that corresponding GW jobs are run on 16, 32, and 64 ranks.

for i in gga hse
do
   for j in 128 256 320
   do
      ./validate.py3 OUTCAR-$i-$j
   done
done

for j in 16 32 64
do
   ./validate.py3 OUTCAR-gw-$j
done

